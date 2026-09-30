#!/usr/bin/env python3
"""从 Claude Code 会话记录（.jsonl）里取出用户的全部原话，按时间编号输出。

用途：走查会话往往很长、中途会被压缩，只靠当前上下文会漏掉前半段的调整。
这个脚本读完整记录，去掉系统提示、工具结果、选中元素的 HTML 和技能正文，
只留下用户真正说的话，方便逐条归类。

用法：
  python3 extract_user_messages.py <session.jsonl> [--max-chars 600]
  python3 extract_user_messages.py --latest <项目记录目录>   # 取最近修改的会话

Claude Code 的会话记录在 ~/.claude/projects/<编码后的项目路径>/<session-id>.jsonl。
"""
import argparse
import glob
import json
import os
import re
import sys

SKIP_PREFIXES = (
    '<system-reminder',
    '<local-command',
    '<command-name>',
    '<command-message>',
    'Base directory for this skill:',
    'This session is being continued',
    '# ',  # 技能 / 命令正文
)


def clean(text: str) -> str:
    text = re.sub(r'<launch-selected-element>.*?</launch-selected-element>',
                  '[选中元素]', text, flags=re.S)
    text = re.sub(r'<system-reminder>.*?</system-reminder>', '', text, flags=re.S)
    text = re.sub(r'</?pasted_content[^>]*>', '', text)
    marker = 'The user sent a new message while you were working:'
    if marker in text:
        text = text.split(marker, 1)[1].split('This is how Claude Code', 1)[0]
    return text.strip()


def iter_user_texts(path):
    with open(path, encoding='utf-8') as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            # 工作中途插入的消息以排队记录保存：{"type": "queue-operation", "operation": "enqueue", "content": "..."}
            if row.get('type') == 'queue-operation':
                if row.get('operation') == 'enqueue' and isinstance(row.get('content'), str):
                    text = clean(row['content'])
                    if text and not text.startswith(SKIP_PREFIXES):
                        yield text
                continue
            # 带截图的插入消息以附件保存：{"attachment": {"type": "queued_command", "prompt": [...]}}
            attachment = row.get('attachment')
            if isinstance(attachment, dict) and attachment.get('type') == 'queued_command':
                prompt = attachment.get('prompt')
                parts = [prompt] if isinstance(prompt, str) else [
                    b.get('text', '') for b in (prompt or [])
                    if isinstance(b, dict) and b.get('type') == 'text'
                ]
                for raw in parts:
                    text = clean(raw)
                    if text and not text.startswith(SKIP_PREFIXES):
                        yield text
                continue
            message = row.get('message') if isinstance(row.get('message'), dict) else {}
            content = message.get('content')
            blocks = []
            if isinstance(content, str):
                blocks = [content]
            elif isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict):
                        continue
                    if block.get('type') == 'text':
                        blocks.append(block.get('text', ''))
                    # 进行中插入的消息会夹在工具结果里
                    if block.get('type') == 'tool_result':
                        inner = block.get('content')
                        if isinstance(inner, str) and 'The user sent a new message' in inner:
                            blocks.append(inner)
                        elif isinstance(inner, list):
                            for sub in inner:
                                if isinstance(sub, dict) and 'The user sent a new message' in sub.get('text', ''):
                                    blocks.append(sub['text'])
            if row.get('type') != 'user' and not any('The user sent a new message' in b for b in blocks):
                continue
            for raw in blocks:
                text = clean(raw)
                if not text or text.startswith(SKIP_PREFIXES):
                    continue
                if text.startswith('[Image: source:'):
                    continue
                yield text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs='?')
    parser.add_argument('--latest', metavar='DIR')
    parser.add_argument('--max-chars', type=int, default=600)
    args = parser.parse_args()

    path = args.path
    if args.latest:
        files = glob.glob(os.path.join(os.path.expanduser(args.latest), '*.jsonl'))
        if not files:
            sys.exit(f'no .jsonl under {args.latest}')
        path = max(files, key=os.path.getmtime)
    if not path:
        parser.error('需要会话记录路径或 --latest <目录>')

    print(f'# {path}')
    seen = set()
    n = 0
    for text in iter_user_texts(path):
        if text in seen:
            continue
        seen.add(text)
        n += 1
        body = text if len(text) <= args.max_chars else text[:args.max_chars] + ' …'
        print(f'{n}. {body}')


if __name__ == '__main__':
    main()
