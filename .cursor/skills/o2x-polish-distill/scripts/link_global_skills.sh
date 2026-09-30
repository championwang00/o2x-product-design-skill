#!/usr/bin/env bash
# 检查并补齐各工具技能库里的 O2X 入口，让它们都软链接到规范仓库（唯一来源）。
# 已存在的真实目录不会被覆盖或删除，只报告出来，由用户决定是否移走备份后改成链接。
#
# 用法：link_global_skills.sh [--fix]
#   不带参数：只检查
#   --fix：为缺失的入口创建软链接
set -u
FIX=0
[ "${1:-}" = "--fix" ] && FIX=1

SKILLS_SRC="$(cd "$(dirname "$0")/../.." && pwd -P)"   # <repo>/.cursor/skills
NAMES=(o2x-product-design o2x-design-system o2x-figma-workflow o2x-polish-distill)
TARGET_DIRS=("$HOME/.claude/skills" "$HOME/.codex/skills" "$HOME/.cursor/skills" "$HOME/.agents/skills")

status=0
for dir in "${TARGET_DIRS[@]}"; do
  [ -d "${dir}" ] || { echo "skip  ${dir}（目录不存在）"; continue; }
  for name in "${NAMES[@]}"; do
    src="$SKILLS_SRC/${name}"
    dst="${dir}/${name}"
    [ -d "${src}" ] || { echo "miss  源目录不存在：${src}"; status=1; continue; }
    if [ -L "${dst}" ]; then
      real="$(cd "${dst}" 2>/dev/null && pwd -P)"
      if [ "${real}" = "${src}" ]; then
        echo "ok    ${dst}"
      else
        echo "WRONG ${dst} -> $(readlink "${dst}")（应指向 ${src}）"; status=1
      fi
    elif [ -e "${dst}" ]; then
      echo "COPY  ${dst} 是独立目录，不是链接；请先移出技能目录备份，再运行 --fix"; status=1
    elif [ $FIX -eq 1 ]; then
      ln -s "${src}" "${dst}" && echo "link  ${dst} -> ${src}"
    else
      echo "none  ${dst}（缺失，--fix 可创建）"; status=1
    fi
  done
done
exit $status
