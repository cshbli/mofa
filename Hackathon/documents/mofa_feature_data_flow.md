# 模法4: 数据流驱动（Dataflow Driven）

与基于工作流(Workflow)的方法不同，MoFa选择基于数据流（Dataflow)的方法。工作流的方法的重心在于对任务的流程和各操作步骤之间业务规则的抽象，而数据流的方法主要是确定任务之间的数据依赖性就可以了。

在各成员智能体之间搭建数据流是MoFA中组合的核心方法。MoFA并不特别关心复杂的业务规则和流程的编排。基本的业务规则在原子智能体模版里就获得了实现，而更复杂的业务规则是成员智能体内部维护，并不暴露在节点和节点之间的流程配置中。流程的编排并不强调管理业务之间顺序，而是数据流动的顺序。正是由于简单和不具“侵入”性的数据流驱动，保障了组合的可叠加和可逆性。在构建复杂应用的过程中，更具备可管理和可调试性。

采用Dataflow而不是Workflow，也是MoFA“模块化”原则和“组合”逻辑的体现。