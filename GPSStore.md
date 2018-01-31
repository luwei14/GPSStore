# GPS数据表达与存储
对于GPS数据，常用的说法有两种，GPS轨迹和GPS点。GPS轨迹是按照运动活动的连贯性和整体性存储的线状实体信息，便于GPS数据的可视化图形化表达。GPS点则是按照GPS接收信号的离散性存储的位置点信息，可以包含高程值，经纬度，时间戳等基本GPS位置状态信息，同时还可以包含速度，心率，步频，踏频等运动主体的状态信息，有利于GPS数据的计算分析。那么在设计数据库存储轨迹数据时要同时考虑这两点特征。