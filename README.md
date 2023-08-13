# 软件源维护 自动化脚本
此项目仅作为学习使用，无其他用途 

## 项目介绍
### 项目设计
#### 总体架构
- icon `存放 app icon, 提交GitHub 作为静态资源服务器` 
  - xxx.png
  - ...
- logs `日志文件目录`
  - xxx.log
  - ...
- other_source `其他源(子)项目` 
  - qingtian `晴天源`
    - source_app `app资源 作中间cache使用`
      - xxx.ipa
      - ...
    - app_info.txt
    - describe.md `子项目描述文件`
    - q_tools.py `晴天源工具`
    - script.py `脚本（入口）`
    - static
  - ...
- source_manage `元元源项目`
  - 

- tools `公用工具集合`
  -- mysql_base.py `mysql 公共工具类`
### 功能介绍
### 更新日志
#### 2023-07-31
a. 完善 `元元源` 添加源功能

### 未来 TODO
a. `元元源` cookie获取

b. 部署服务器运行

c. app icon api开发

d. `晴天源`源名称优化

e. `晴天源`app url 获取优化

f. 日志记录
## 联系我们

[软件源地址](2274466264@qq.com)

[发卡地址]()

[使用教程]()

[联系我们](2274466264@qq.com)
