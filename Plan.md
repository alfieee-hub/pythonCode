# 一、详细计划

## ✅ 阶段一：基础打牢

### 📘 Python

- ✅ 推荐掌握程度：中高级（能独立完成数据处理、调用 API、构建项目脚本）
- 🧩 核心知识点：
  - 基础语法：变量、控制流、函数、类与对象
  - 数据结构：list、tuple、dict、set 的使用与区别
  - 函数式编程：lambda、map、filter、reduce
  - 模块与包管理：import、自定义模块、`requirements.txt`
  - 异常处理：try-except、异常链
  - 文件操作：with open、读取 JSON/CSV/YAML
  - 环境管理：venv/conda、pip
- ⚠️ 重难点：
  - 可变对象引用机制（list 复制陷阱）
  - 装饰器、迭代器、生成器的原理与实际使用
  - 多线程与多进程（GIL 限制，ThreadPoolExecutor vs ProcessPoolExecutor）

------

### 📘 Pandas

- ✅ 推荐掌握程度：中高级（能熟练清洗、处理并生成分析报告）
- 🧩 核心知识点：
  - 核心对象：`Series`, `DataFrame`
  - 数据导入导出：`read_csv`、`to_excel`、`read_json`
  - 索引与切片：loc / iloc、布尔索引
  - 数据处理：缺失值处理、类型转换、重命名、分组聚合（`groupby`）
  - 合并操作：`concat`, `merge`, `join`, `append`
  - 时间序列处理：`resample`, `rolling`, `dt` 属性
  - 应用函数：`apply`, `map`, `agg`, `transform`
- ⚠️ 重难点：
  - groupby 的 transform 与 agg 区别
  - 多层索引（MultiIndex）处理逻辑
  - apply 性能问题（尽量向量化）

------

### 📘 NumPy

- ✅ 推荐掌握程度：中级（掌握矩阵运算 + 基础统计分析）
- 🧩 核心知识点：
  - 多维数组对象 `ndarray` 的创建与操作
  - 数组切片、布尔索引、广播机制
  - 常见函数：`reshape`, `transpose`, `sum`, `mean`, `std`
  - 随机数模块：`np.random`, `seed`
  - 矩阵运算：点乘、内积、逆矩阵
- ⚠️ 重难点：
  - 广播规则（shape 自动扩展机制）
  - 高维数组变换逻辑
  - 数据类型（dtype）转换陷阱

------

### 📘 Matplotlib

- ✅ 推荐掌握程度：中级（掌握常见图表绘制 + 图形美化）
- 🧩 核心知识点：
  - 基本图形：折线图、柱状图、散点图、直方图
  - 子图排布：`subplot`, `subplots`, `GridSpec`
  - 图例、标题、坐标轴设置
  - 样式：颜色、线型、注释、中文显示处理
  - 与 Pandas 集成绘图（`.plot()`）
- ⚠️ 重难点：
  - 多子图共享坐标轴设置
  - 中文乱码与图像保存参数
  - 三维图、双坐标轴等高级图示

------

### 📘 Linux & Shell

- ✅ 推荐掌握程度：中级（熟悉系统操作 + 能写常用运维脚本）
- 🧩 核心知识点：
  - 常用命令：`ls`, `grep`, `find`, `awk`, `sed`, `xargs`, `sort`, `uniq`
  - 文件权限与路径操作：`chmod`, `chown`, `ln`, `pwd`, `cd`
  - Bash 语法：变量定义、if、for、while、函数定义
  - 进程与服务管理：`ps`, `top`, `kill`, `systemctl`
  - 文件处理：`cat`, `tee`, `cut`, `split`, `tr`
- ⚠️ 重难点：
  - `awk`, `sed` 脚本编写的语法掌握（正则结合逻辑）
  - 管道与重定向组合技巧（`|`, `>`, `>>`, `<`）
  - crontab 定时任务的配置语法

------

### 📘 MySQL

- ✅ 推荐掌握程度：中高级（能熟练编写 SQL + 分析执行计划 + 调优）
- 🧩 核心知识点：
  - DDL/DML 基础：`CREATE`, `INSERT`, `UPDATE`, `DELETE`
  - 查询语法：`SELECT`, `WHERE`, `GROUP BY`, `JOIN`, `HAVING`
  - 索引原理：B+ 树索引、覆盖索引、联合索引、最左前缀
  - 执行计划分析：`EXPLAIN` 解读
  - 常用函数：窗口函数、日期函数、字符串函数
  - 事务控制：ACID 原则、隔离级别（RR、RC）
- ⚠️ 重难点：
  - 查询优化：避免全表扫描、合理使用索引
  - 死锁分析与事务设计
  - 多表关联优化策略（驱动表选取、临时表/子查询）

------

## ✅ 阶段二：数据工程构建

### 📘 PySpark

- ✅ 推荐掌握程度：中高级（能独立开发复杂分布式数据处理任务）
- 🧩 核心知识点：
  - Spark 基础架构（Driver、Executor、Cluster Manager）
  - RDD 基础与高级转换（map、filter、reduceByKey、groupByKey）
  - DataFrame 与 Dataset API（select、filter、agg、join）
  - Spark SQL：写SQL查询，注册临时视图
  - UDF（用户自定义函数）开发与注册
  - 容错机制和任务调度流程
  - Shuffle 机制及其性能影响
  - 数据倾斜问题及解决方案（salting、broadcast join）
  - 数据序列化与存储格式（Parquet、ORC等）
- ⚠️ 重难点：
  - 理解 Spark 的延迟执行和触发机制
  - Shuffle 过程中网络和磁盘I/O瓶颈排查
  - 处理数据倾斜和内存溢出
  - 高效编写UDF，避免性能下降
  - Spark Streaming 与批处理的区别和应用

------

### 📘 Kafka

- ✅ 推荐掌握程度：中高级（能搭建、使用并调优 Kafka 集群）
- 🧩 核心知识点：
  - Kafka 架构（Broker、Topic、Partition、Consumer Group）
  - Producer 和 Consumer API
  - 消息可靠性与幂等性保证
  - 复制机制与 ISR 集合
  - Kafka Connect 和 Kafka Streams
  - 消息压缩与序列化（Avro、JSON、Protobuf）
  - Offset 管理和消费位点提交
- ⚠️ 重难点：
  - 消息顺序保证和重复消费处理
  - Broker 故障恢复与 Leader 选举
  - 高吞吐量配置与性能调优
  - 跨集群复制与多租户隔离

------

### 📘 Flink

- ✅ 推荐掌握程度：高级（流式数据实时处理专家）
- 🧩 核心知识点：
  - Flink 核心架构（JobManager、TaskManager）
  - DataStream API：转化、窗口、状态
  - 状态管理与状态后端（RocksDB）
  - 时间语义（Event Time、Processing Time）
  - Watermark 机制
  - Checkpoint 和故障恢复
  - 复杂事件处理 (CEP)
- ⚠️ 重难点：
  - Exactly-once 语义实现
  - 状态大小和性能调优
  - 大规模状态持久化和恢复
  - 延迟数据处理与窗口触发策略

------

### 📘 Canal

- ✅ 推荐掌握程度：中级（掌握数据库变更捕获和同步原理）
- 🧩 核心知识点：
  - MySQL Binlog 结构与原理
  - Canal 订阅机制与数据抓取流程
  - 数据同步配置（canal-server、canal-adapter）
  - 与 Kafka、Elasticsearch 等系统集成
- ⚠️ 重难点：
  - Binlog 解析性能与资源消耗
  - 事务边界识别与数据一致性保证
  - 断点续传与异常恢复
  - 多实例多库同步管理

------

### 📘 scikit-learn

- ✅ 推荐掌握程度：中级（经典机器学习模型构建的主力库）
- 🧩 核心知识点：
  - 数据预处理模块（`StandardScaler`, `OneHotEncoder` 等）
  - 模型训练流程（`fit` / `predict` / `score` / `cross_val_score`）
  - 常用模型（逻辑回归、SVM、随机森林、KMeans、PCA）
  - 管道机制（Pipeline）与参数搜索（GridSearchCV / RandomizedSearchCV）
  - 模型评估指标（accuracy, precision, recall, ROC-AUC）
- ⚠️ 重难点：
  - 特征工程与数据清洗的配合流程设计
  - 模型调参与过拟合控制（正则化、交叉验证）
  - 自定义评估函数与组合管道的使用
  - 与 Pandas / NumPy 数据结构的衔接和性能优化

------

### 📘 MongoDB

- **推荐掌握程度**：中级（能熟练使用在项目中，了解其索引、聚合和存储原理）
- **核心知识点**：
  - 基础操作：CRUD、更新、删除、upsert；
  - 索引机制：单字段索引、复合索引、唯一索引、TTL 索引；
  - 聚合管道：`$match`、`$group`、`$project`、`$lookup`；
  - Schema 设计原则：扁平化嵌套文档、冗余字段优化读性能；
  - 数据类型：ObjectId、数组、嵌套文档；
  - ReplicaSet、Sharding 的基本原理；
  - Python 中的 PyMongo 使用；
- **重难点**：
  - 聚合管道的组合逻辑与性能调优；
  - 如何为查询设计高效索引（避免全表扫描）；
  - 大数据量下的性能优化（分页、游标、limit+sort）；
  - 与传统 RDBMS 思维差异（无事务或弱事务模型）；
  - 分片集群构建及跨分片 JOIN 限制；

------

### 📘 Doris

- ✅ 推荐掌握程度：中级（作为高性能分析型数据库，适合实时 BI 场景）
- 🧩 核心知识点：
  - 架构组件（Frontend、Backend 节点职责）
  - 数据模型（Key 模型、Unique 模型、Duplicate 模型）
  - 数据导入方式（Stream Load、Broker Load、Routine Load、Insert into）
  - SQL 支持范围（兼容 MySQL 的语法、窗口函数、Join 优化等）
  - 列式存储、压缩与向量化执行引擎
- ⚠️ 重难点：
  - 多副本一致性与容灾恢复机制
  - 实时写入调优（例如 Routine Load 的吞吐、批量策略）
  - 高并发查询下的性能优化（分区、桶划分、谓词下推）
  - 集群部署、自动伸缩与资源隔离

------

### 📘 Superset

- ✅ 推荐掌握程度：基础到中级（会用其进行数据可视化和简单仪表盘设计）
- 🧩 核心知识点：
  - 数据连接与权限管理
  - 仪表盘创建与交互设计
  - 图表类型与参数配置
  - SQL Lab 进行数据查询
- ⚠️ 重难点：
  - 大数据量可视化性能调优
  - 自定义图表插件开发
  - 多租户权限和安全策略

------

### 📘 Hudi

- ✅ 推荐掌握程度：中级（掌握流批一体的数据湖写入和管理）
- 🧩 核心知识点：
  - 数据湖概念与增量写入
  - Copy-on-Write 和 Merge-on-Read 存储模式
  - 索引机制与数据合并策略
  - 时间旅行查询（Snapshot Reads）
  - 与 Spark、Flink 集成
- ⚠️ 重难点：
  - 并发写入冲突处理
  - 压缩与合并任务调度
  - 大规模数据的元数据管理

------

### 📘 Iceberg

- ✅ 推荐掌握程度：中级（掌握大规模数据湖表管理）
- 🧩 核心知识点：
  - 表格式和版本控制
  - 快速表扫描和分区裁剪
  - 增量数据读取和写入
  - Schema 演进与分区演进
  - 与 Spark、Presto、Trino 集成
- ⚠️ 重难点：
  - 元数据管理与性能优化
  - 多版本数据一致性
  - 跨工具链的数据操作兼容性

------

### 📘 数据存储格式（Parquet / ORC / Avro）

- ✅ 推荐掌握程度：基础到中级（理解列式存储及序列化格式原理）
- 🧩 核心知识点：
  - 列式存储结构与优势
  - Parquet 文件格式结构（页、列块、文件元数据）
  - ORC 文件压缩与索引技术
  - Avro 序列化机制与 schema 管理
  - 读取和写入接口
- ⚠️ 重难点：
  - 压缩算法对性能的影响
  - Schema 演进和兼容性处理
  - 大文件分片与并行读写

------

## ✅ 阶段三：调度监控与中台管理

### 📘 Dagster

- ✅ 推荐掌握程度：中级（理解数据编排概念，能设计和管理任务流水线）
- 🧩 核心知识点：
  - 核心对象：Op、Graph、Job、Pipeline
  - 任务依赖管理与输入输出定义
  - 任务调度与事件触发（Scheduler、Sensor）
  - 日志与监控集成
  - 资源管理与配置
- ⚠️ 重难点：
  - 动态任务构建与复用
  - 失败重试机制设计
  - 与外部系统（数据库、消息队列）集成
  - 数据血缘追踪和版本控制

------

### 📘 Airflow

- ✅ 推荐掌握程度：中高级（掌握工作流调度和任务依赖管理）
- 🧩 核心知识点：
  - DAG（有向无环图）定义与调度机制
  - 任务编排与依赖设置（`PythonOperator`, `BashOperator` 等）
  - 任务重试、失败处理与 SLA 设置
  - 插件机制、连接管理与外部服务集成（MySQL、S3、Kafka 等）
  - Web UI 使用与日志调试、任务优先级与资源池设置
- ⚠️ 重难点：
  - DAG 动态生成与模块化组织
  - 调度器性能调优与分布式部署（CeleryExecutor、KubernetesExecutor）
  - 跨 DAG 通信、任务并发控制与任务间依赖设计
  - 多环境部署（开发、测试、生产）与 CI/CD 集成

------

## ✅ 阶段四：AI 应用支撑

### 📘 FAISS

- ✅ 推荐掌握程度：中级（理解向量检索原理，能完成向量索引搭建和查询）
- 🧩 核心知识点：
  - 向量相似度计算（欧氏距离、余弦相似度）
  - 索引类型：Flat、IVF、PQ、HNSW
  - 索引构建流程及参数调优
  - 向量量化与压缩原理
  - 批量插入和查询接口使用
  - GPU 加速版本的使用
- ⚠️ 重难点：
  - 理解不同索引结构的空间和时间权衡
  - 向量预处理（归一化、降维）
  - 调优索引参数以平衡召回率和查询速度
  - 大规模向量的内存管理与存储
  - 实时动态更新索引的复杂性

------

### 📘 Milvus

- ✅ 推荐掌握程度：中级（能搭建和使用向量数据库，支持向量检索服务）
- 🧩 核心知识点：
  - 向量数据存储与索引原理
  - Milvus 架构（Proxy、DataNode、IndexNode 等）
  - 向量插入、搜索及管理 API
  - 支持的索引类型（IVF、HNSW、ANNOY）
  - 集群部署与负载均衡
  - 与FAISS等向量库的区别与结合
- ⚠️ 重难点：
  - 向量数据高效存储与索引优化
  - 向量搜索精度与性能平衡
  - 集群扩展与故障恢复
  - 多模态数据管理及扩展支持

------

### 📘 Embedding 技术原理

- ✅ 推荐掌握程度：中级（理解向量表示与语义编码）
- 🧩 核心知识点：
  - 词向量（Word2Vec、GloVe）训练原理
  - 句向量与文档向量编码技术（SBERT、SimCSE）
  - 向量距离度量（欧氏、余弦相似度）
  - 向量索引结构与近似搜索算法
- ⚠️ 重难点：
  - 向量空间的语义保持与泛化能力
  - 训练语料选择对效果的影响
  - 向量检索效率与存储成本平衡

------

### 📘 LangChain

- ✅ 推荐掌握程度：基础（了解链式调用大模型的设计思路）
- 🧩 核心知识点：
  - Prompt 模板设计
  - 链（Chain）的定义和构建
  - 记忆（Memory）机制
  - 与外部工具或API的集成
- ⚠️ 重难点：
  - 长上下文管理和截断策略
  - 多任务异步协调
  - 错误处理与异常恢复

------

### 📘 RAG（Retrieval-Augmented Generation）

- ✅ 推荐掌握程度：基础（理解检索增强生成框架原理）
- 🧩 核心知识点：
  - 向量检索与文本检索结合
  - 知识库构建与管理
  - 生成模型结合检索结果流程
  - 多轮对话上下文利用
- ⚠️ 重难点：
  - 实时检索结果质量控制
  - 检索延迟对生成性能影响
  - 跨模态检索与生成

------

## ✅ 阶段五：系统部署与工程化

### 📘 Docker

- ✅ 推荐掌握程度：中级（能写 Dockerfile，搭建容器环境及调试）
- 🧩 核心知识点：
  - 容器基本概念与镜像构建流程
  - Dockerfile 语法（FROM、RUN、COPY、CMD）
  - 镜像层和缓存机制
  - 容器网络模型（bridge、host、overlay）
  - 数据卷（Volumes）与持久化
  - Docker Compose 多容器编排
  - 容器调试（日志、交互式Shell）
- ⚠️ 重难点：
  - 优化镜像大小（多阶段构建、缓存利用）
  - 容器安全与权限控制（用户、能力限制）
  - 容器与宿主机资源隔离和限制
  - 网络复杂配置及端口映射冲突
  - 数据卷备份与恢复策略

------

### 📘 Kubernetes

- ✅ 推荐掌握程度：中级（能部署和管理容器集群，理解基本资源对象）
- 🧩 核心知识点：
  - 核心概念：Pod、Node、Deployment、Service
  - 控制器模式（ReplicaSet、StatefulSet、DaemonSet）
  - ConfigMap 和 Secret 管理配置与敏感数据
  - Service 类型（ClusterIP、NodePort、LoadBalancer）
  - 资源调度（Node Affinity、Taints & Tolerations）
  - 自动伸缩（Horizontal Pod Autoscaler）
  - 存储卷类型与持久化存储
  - 基本网络模型和服务发现
- ⚠️ 重难点：
  - 集群安装与高可用配置
  - 复杂调度策略和资源配额管理
  - 安全机制（RBAC、NetworkPolicy）
  - 日志采集与集群监控
  - Helm Chart 编写和包管理

------

### 📘 API与模型部署

- ✅ 推荐掌握程度：中级（能构建基础模型服务API并部署）
- 🧩 核心知识点：
  - Flask、FastAPI 框架基础
  - 模型序列化与加载（pickle、TorchScript、ONNX）
  - Docker 容器化部署
  - 模型服务的监控与日志
  - 负载均衡与限流
- ⚠️ 重难点：
  - 模型版本管理与热更新
  - 高并发访问性能调优
  - 异常处理与熔断机制设计