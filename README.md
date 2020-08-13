
语音合成小助手

功能：一键将文本转为语音并导出mp3文件



![main](/screeshots/main.png)



## 使用说明

1 点击 **合成语音** 按钮后，会自动在本地创建一个audio文件夹，转换完成的mp3文件就在这里，命名格式为：`当前时间+文本的前10个字.mp3`,例如`2020-02-25_22-29-37欢迎使用百度语音合成.mp3`

2 使用的是百度语音合成api，最多只能转换512个汉字(1024个字节)

## 安装说明

### 普通使用

如果你只是想使用这个小工具，请直接下载windows可执行文件压缩包。

[点击下载](https://github.com/xugongli/Text2Speech/releases/download/1.0/zip_for_windows.7z)

解压后是一个exe可执行文件，直接打开即可使用。这也是写这个小工具的契机。

### 开发者使用

如果你熟悉python,以下是启动流程

1 使用以下指令clone到本地

`git clone https://github.com/xugongli/Text2Speech.git `

2 安装依赖,这个工具只使用到了pyqt5和baidu-aip两个库

` pip install -r requirements.txt`

3 启动

`python main.py`

如果你是windows环境，双击`打开语音合成助手.bat`也可。

## 联系我

如果在使用过程中遇到无法解决的问题，你可以通过关注我的个人公众号找到我。

另外，也可以通过提交issue的方式提交问题。

![rewnwen_wechat](./screeshots/rewnwen_wechat.png)

