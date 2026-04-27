from PIL import Image
import os

def convert_to_proper_ico(png_path, ico_path):
    try:
        # 1. 以 RGBA 模式打开，保留透明度
        src_img = Image.open(png_path).convert("RGBA")

        # 2. 预先生成高质量缩放后的图像列表
        # 使用 Resampling.LANCZOS 替代默认缩放，这是保持清晰的关键
        icon_list = []
        sizes = [16, 32, 48, 64, 128, 256]

        for size in sizes:
            # 采用高质量重采样算法
            resized_img = src_img.resize((size, size), Image.Resampling.LANCZOS)
            icon_list.append(resized_img)

        # 3. 保存时直接传入处理好的图像列表
        # 第一个图像通常作为主图，其它的存入图层容器
        icon_list[-1].save(ico_path, format='ICO', append_images=icon_list)

        print(f"✓ 高清图标转换成功: {ico_path}")
        return True
    except Exception as e:
        print(f"✗ 转换失败: {e}")
        return False

if __name__ == "__main__":
    png_file = "ico.png"
    ico_file = "icon.ico"

    if os.path.exists(png_file):
        print(f"正在将 {png_file} 转换为 {ico_file}...")
        convert_to_proper_ico(png_file, ico_file)
    elif os.path.exists(ico_file):
        print(f"检测到现有的 {ico_file}，尝试重新转换...")
        try:
            img = Image.open(ico_file)
            print(f"当前图标格式: {img.format}, 尺寸: {img.size}")

            if img.format != 'ICO':
                print("格式不正确，正在重新转换...")
                # 使用新的高清转换方式
                convert_to_proper_ico(png_file, ico_file)
                print("✓ 图标已重新转换")
            else:
                print("✓ 图标格式正确")
        except Exception as e:
            print(f"✗ 无法读取图标文件: {e}")
    else:
        print("✗ 未找到图标文件")
