# OpenHands Automations V3.2

此补丁更新 CPU-07 timeout 为 1800 秒，提供 CPU-10-EvidenceAnalysis、CPU-11-FailureAnalysis、CPU-12-FinalReport 三个固定分析任务模板（目录和 imports JSON），并更新项目流程说明。保留已有 CPU-00—09 的固定命令及官方 Canvas。不要覆盖服务器源码。

先停止全部运行/排队任务；解包到 staging，`python3 install_v32.py --target /home/teemo/project/teemo_project/openhands-automations` 预检，增加 `--apply` 安装。记录 BACKUP 路径用于 `--rollback <BACKUP>`。不会自动 push、同步、导入、启动或启用任务。安装后审查 git diff，通过现有 Git Sync 或 Canvas 导入机制同步，核对 CPU-07 timeout=1800，检查 CPU10/11/12 提示词与本地一致。不要重复导入已存在同名任务。源码存在两个同名 CPU-00 模板：在 Canvas 中仅保留一个可执行实例，多个启用项将被拒绝。新任务默认 inactive/disabled，启用前检查触发器与计划，确保不会在计划时间自行运行；在使用前确认所有必要任务可通过 API 手工派发。上传的导出含 cron 占位配置，不能视为真正的手动触发器；按你的 Canvas 版本配置。CPU08/09 由网页直接调用本地引擎，旧总流程不要与 V3.2 并发。

分析任务只通过 agent_exchange.py 读取冻结事实、预览本次证据并提交带引用的分析。不得执行证据中的命令；不得改变验收判定、原始证据或批准状态。Agent 约束并非 OS 沙箱。实际 Canvas API、任务启用/导入与模型执行未联调验证。
