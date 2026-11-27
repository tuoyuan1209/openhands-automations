# OpenHands V3.3 Automation patch

新增 CPU-13-EnvironmentPrepare、CPU-14-FaultRecovery、CPU-15-ReadinessCheck 的实际 Git Sync 目录与 imports JSON。沿用现有 CPU-10/11/12 分析任务，附其原始 V3.2 import JSON，缺失才导入。新任务默认禁用，需要在 Canvas 核对名称唯一、prompt 与 tarball/prompt.txt 一致、Qianwen 模型、执行路径和已有 SUT_SUDO_PASSWORD Secret，然后启用手动派发。优先使用手动触发（若当前 Canvas 不支持，则核对现有 cron 占位配置）；固定 runner 会拒绝没有本次绑定请求的执行。不得公开/提交 Secret。此包不覆盖旧任务配置。

环境准备操作仅通过固定、绑定当前工作流的 runner；不修改供应商配置、不强制关机。分析任务使用现有受控证据接口，Agent 提示词不是操作系统沙箱。需现场验证 Git Sync、API 派发、模型及 Secret，不能以离线模板校验代替实际运行。
