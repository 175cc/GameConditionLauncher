@echo off
chcp 65001 >nul
echo ================================
echo 游戏条件启动器 - 打包工具
echo ================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未检测到Python，请先安装Python
    pause
    exit /b 1
)

echo [1/4] 正在安装依赖...
pip install -r requirements.txt
if errorlevel 1 (
    echo 错误: 依赖安装失败
    pause
    exit /b 1
)
echo ✓ 依赖安装完成!
echo.

echo [2/4] 正在检查并转换图标...
python convert_icon.py
if errorlevel 1 (
    echo ⚠ 警告: 图标转换失败，将不使用自定义图标
)
echo.

echo [3/4] 正在打包应用程序...
python build_exe.py
if errorlevel 1 (
    echo 错误: 打包失败
    pause
    exit /b 1
)
echo.

echo [4/4] 打包完成!
echo.
echo ================================
echo ✓ 成功! 
echo 可执行文件位置: dist\游戏条件启动器.exe
echo ================================
echo.
echo 注意: 请以管理员身份运行生成的exe文件
echo.
pause
