# OpenHands Automation V2 — 供应商KVM验收

对应现有 `tuoyuan1209/openhands-automations`，不是新仓库。依赖平级的 `cpu_ai_validation` V2 测试执行仓库。11套任务（00–09 + 总流程）。原6个目录保留同名，CPU-02-Provision 现为只读预检。所有定义默认 inactive/disabled，保留原 cron 字段（每年1月1日00:00，不是“手动”触发类型）。如启用任务，务必检查实际定时调度。只使用 Run now，或直接运行固定脚本。

## 方式A：继续你已有的Git Sync（推荐，二选一）

1. 在 Canvas 停止旧任务和临时关闭 Git Sync。确认无旧脚本仍在执行。Git Sync 双向同步且同一任务存在本地未同步修改时，本地修改可能优先；先备份/同步尚未入库的 CPU-00、06 等任务。
2. 将压缩包解压至独立目录，运行 `python3 install_upgrade.py`（dry-run）；确认目标路径后再 `python3 install_upgrade.py --apply`。只覆盖仓库内相关文件，备份旧文件，不自动提交。
3. 在目标仓库执行 `git status`, `git diff`, `git diff --stat`，查看新增目录。不要覆盖未保存的 UI 修改。建议分支/PR 审核后合并到 Canvas 实际同步分支，然后恢复 Git Sync，点击 Sync now。
4. 在 Canvas 验证名称、Prompt、Local 后端、qianwen 模型、Timeout、Secret 访问、停用状态。先手动运行 CPU-00 或 CPU-01 小范围验证。勿同时导入下述 JSON，以免重复任务。

同步目录是 `automations/`。`imports/` 为便携文件备份，不应配置为 Git Sync 路径。`workflows/` 是项目流程描述，不是 Canvas 原生 workflow DSL。

## 方式B：Canvas Import automation

`imports/*.automation.json` 使用官方文档的 version 1 prompt 自动化格式，UI Automate > Import automation 逐个导入并预览。导入会新建任务，不一定更新已有任务；已有同名任务先停用，不要重复启动。Git 目录保留了用户上传的 `main.py`, `finish_tool_hook.py`, `setup.sh`（共享 runtime 补丁）并替换 Prompt。便携 JSON 导入由 Canvas 生成 preset runner，不保证使用归档内补丁；你之前已经修改了本机 runner preset，请检查导入任务的实际 setup。导入接口和 Git Sync 均未在你实际 Canvas 1.45.0 / Automation 1.35.0 上联调，首次先测试一个任务。

固定 Python 路径 `/root/.cache/uv/archive-v0/OvJCewHopHDXy8xF/bin/python` 沿用实际模板；升级 SDK 后该路径可能变化，需要统一调整。Secret `SUT_SUDO_PASSWORD` 继续使用 Canvas 现有管理，不写入任何 JSON/YAML。无需将测试仓库再次 clone 进 Automation sandbox，脚本通过已挂载的共享工程路径执行。

CPU-08 Stability 在 Canvas 中只读取结果：现有 1800 秒任务上限不适合 3600 秒连续测试。实际长测在持久终端运行 `scripts/run_stage.py 08 --allow-long`。CPU-09 汇总经批准会话的证据，缺少08时不能给整体PASS。总流程任务执行01、00、02–07，遇 FAIL/INCONCLUSIVE 停止，仍输出部分报告。不要通过增加模型分析时间解决固定脚本的非PASS结果。

官方格式说明：https://docs.openhands.dev/openhands/usage/agent-canvas/managing-automations
Git同步：https://docs.openhands.dev/openhands/usage/agent-canvas/git-sync
