import tkinter as tk  #python的标准库，用于创建图形用户界面
from datetime import datetime  #获取当前时间
import getpass  #获取当前登录的系统用户名


def create_watermark():
    # 获取系统登录的用户名
    username = getpass.getuser()

    # 创建主窗口
    root = tk.Tk()
    root.title("Watermark")

    # 将窗口置于最上层
    root.attributes('-topmost', True)

    # 设置全屏窗口
    root.attributes('-fullscreen', True)

    # 设置透明背景
    root.attributes('-alpha', 0.3)

    # 禁止调整大小
    root.resizable(False, False)

    # 允许点击穿透窗口
    root.attributes('-transparentcolor', root['bg'])

    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 创建画布
    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()

    # 设置字体样式
    font = ("Arial", 50, "bold")  # 字体稍微大一些

    # 水印文本样式
    text_color = 'gray'
    rotation_angle = 45  # 设置水印旋转角度

    def update_watermark():
        # 获取当前时间，格式化到分钟
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        # 清空画布
        canvas.delete("all")

        # 水印内容
        watermark_content = f"{username} {current_time}"

        # 定义水印的位置（屏幕中央）
        x = screen_width // 2
        y = screen_height // 2

        # 绘制水印
        canvas.create_text(x, y, text=watermark_content, font=font, fill=text_color, angle=rotation_angle,
                           anchor='center')

        # 每分钟更新一次（更新时间）
        root.after(60000, update_watermark)

    # 初次调用，开始循环
    update_watermark()

    # 运行窗口
    root.mainloop()


# 调用
create_watermark()
