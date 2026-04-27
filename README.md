# 游戏条件启动器

一个基于 Tkinter 的简单 GUI 应用程序，用于根据特定条件启动程序或游戏，包括临时修改系统时间。
tips：自用单机QQ飞车单机版（60帧有破风特效），资源收集网路，只是需要特定条件运行断网和时间限制。所以写了个小玩意，AI写的。别狗叫了，能用就行。需要的可以拿去用，或者改改。需要管理员权限运行。
下面是游戏资源，资源来源于网络，与本人无关，仅限学习用，务必下载测试24小时内删除。
夸克网盘链接：https://pan.quark.cn/s/f554366ba67e?pwd=v5Mr 提取码：v5Mr


## 功能
- 浏览并选择可执行文件 (.exe)
- 临时修改系统时间到用户指定的日期时间（默认 2026-01-08）
- 启动选定的程序（不修改时间）
- 从网络同步并恢复到最新的北京时间（UTC+8）

## 要求

- Python 3.x
- Tkinter（Python 标准库中包含）
- ntplib（用于时间同步）
- **管理员权限**（Windows 上修改系统时间需要）

## 安装

1. 克隆或下载仓库。
2. 确保 Python 已安装。
3. 以管理员身份运行应用程序：右键点击 `GameConditionLauncher.py` 并选择“以管理员身份运行”，或在提升权限的命令提示符中使用 `python GameConditionLauncher.py`。

## 使用

1. 点击“浏览...”选择要运行的程序。
2. 在左侧输入框中设置所需的时间（年月日时分秒），点击“确认修改时间”来临时修改系统时间。
3. 点击“启动前【请改时间】【请断网】”启动程序（不修改时间）。
4. 点击“恢复时间”从网络同步到最新的北京时间。

## 注意事项

- 系统时间仅在用户手动修改时改变。
- 恢复时间需要网络连接以同步 NTP 时间。
- 此工具适用于测试或绕过软件中的日期限制。
- 确保在需要时备份或同步准确时间。

## 未来增强

- 添加启动前的条件检查
- 支持多个程序
- 配置文件用于启动设置
- 自定义日期选择

---

# Game Condition Launcher

A simple GUI application built with Tkinter to launch programs or games based on certain conditions, including temporarily changing the system time.
Tips: For personal use with standalone QQ Speed single-player version (60fps with wind-breaking effects), resources collected from the internet, just need specific conditions to run offline and time restrictions. So I wrote a small tool, AI-written. Don't complain, it works. If you need it, take it and use it, or modify it. Requires administrator privileges to run.
Below is the game resource, sourced from the internet, unrelated to me, for learning purposes only, must delete within 24 hours after downloading and testing.
Quark cloud disk link: https://pan.quark.cn/s/f554366ba67e?pwd=v5Mr Extraction code: v5Mr

## Features

- Browse and select executable files (.exe)
- Temporarily change system time to user-specified date and time (default 2026-01-08)
- Launch the selected program (without changing time)
- Sync and restore to the latest Beijing time (UTC+8) from the network

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)
- ntplib (for time synchronization)
- **Administrator privileges** (required for changing system time on Windows)

## Installation

1. Clone or download the repository.
2. Ensure Python is installed.
3. Run the application as administrator: Right-click on `GameConditionLauncher.py` and select "Run as administrator" or use `python GameConditionLauncher.py` in an elevated command prompt.

## Usage

1. Click "浏览..." (Browse) to select the program you want to run.
2. In the left input fields, set the desired time (year, month, day, hour, minute, second), click "确认修改时间" (Confirm Set Time) to temporarily change the system time.
3. Click "启动前【请改时间】【请断网】" (Launch Program) to start the program (without changing time).
4. Click "恢复时间" (Restore Time) to sync to the latest Beijing time from the network.

## Notes

- The system time is changed only when manually set by the user.
- Restoring time requires network connection for NTP synchronization.
- This tool is intended for testing or bypassing date-based restrictions in software.
- Ensure you have backup or synchronization for accurate time if needed.

## Future Enhancements

- Add condition checks before launching
- Support for multiple programs
- Configuration files for launch settings
- Custom date selection
