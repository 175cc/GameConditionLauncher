import PyInstaller.__main__
import os
import sys

def build_exe():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    icon_path = os.path.join(current_dir, 'icon.ico')
    
    args = [
        'GameConditionLauncher.py',
        '--name=游戏条件启动器',
        '--onefile',
        '--windowed',
        '--hidden-import=tkinter',
        '--clean',
        '--noconfirm',
        f'--distpath={os.path.join(current_dir, "dist")}',
        f'--workpath={os.path.join(current_dir, "build")}',
        f'--specpath={current_dir}',
    ]
    
    if os.path.exists(icon_path):
        args.append(f'--icon={icon_path}')
        print(f"✓ 使用图标: {icon_path}")
    else:
        print("⚠ 警告: 未找到icon.ico，将使用默认图标")
    
    print("=" * 60)
    print("开始打包应用程序...")
    print("=" * 60)
    print("参数:", ' '.join(args))
    print()
    
    PyInstaller.__main__.run(args)
    
    print()
    print("=" * 60)
    print("✓ 打包完成！")
    exe_path = os.path.join(current_dir, 'dist', '游戏条件启动器.exe')
    print(f"可执行文件位于: {exe_path}")
    print("=" * 60)

if __name__ == "__main__":
    build_exe()
