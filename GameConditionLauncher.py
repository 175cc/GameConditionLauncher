import tkinter as tk
from tkinter import filedialog, messagebox
import ctypes
import subprocess
import threading
import ntplib
from datetime import datetime, timedelta

# 全局变量：目标软件运行地址
TARGET_PROGRAM_PATH = ""


class GameConditionLauncher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("游戏条件启动器")
        self.geometry("500x300")  # 增加高度以容纳提示文字
        # 选择程序路径
        self.program_path = tk.StringVar()
        tk.Label(self, text="要运行的应用程序:").grid(row=0, column=0, sticky="w", padx=10, pady=10)
        tk.Entry(self, textvariable=self.program_path, width=50).grid(row=0, column=1, padx=5)
        tk.Button(self, text="浏览...", command=self.browse_program).grid(row=0, column=2, padx=5)
        # 保存原始时间
        self.original_time = self.get_system_time()
        # 启动按钮（仅启动程序，不修改时间）
        tk.Button(self, text="启动前【请改时间】【请断网】", command=self.launch_program).grid(row=1, column=0, columnspan=3, pady=10)
        # 预留下方区域
        self.left_frame = tk.Frame(self)
        self.left_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.right_frame = tk.Frame(self)
        self.right_frame.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # 获取当前系统时间的时分秒
        current_hour = str(self.original_time[3])
        current_min = str(self.original_time[4])
        current_sec = str(self.original_time[5])

        # 左侧：修改时间（年月日等单位放在输入框后面）
        self.year_var = tk.StringVar(value="2026")
        self.month_var = tk.StringVar(value="1")
        self.day_var = tk.StringVar(value="8")
        self.hour_var = tk.StringVar(value=current_hour)
        self.min_var = tk.StringVar(value=current_min)
        self.sec_var = tk.StringVar(value=current_sec)
        tk.Entry(self.left_frame, textvariable=self.year_var, width=5).grid(row=0, column=0)
        tk.Label(self.left_frame, text="年").grid(row=0, column=1, sticky="w")
        tk.Entry(self.left_frame, textvariable=self.month_var, width=3).grid(row=0, column=2)
        tk.Label(self.left_frame, text="月").grid(row=0, column=3, sticky="w")
        tk.Entry(self.left_frame, textvariable=self.day_var, width=3).grid(row=0, column=4)
        tk.Label(self.left_frame, text="日").grid(row=0, column=5, sticky="w")
        tk.Entry(self.left_frame, textvariable=self.hour_var, width=3).grid(row=0, column=6)
        tk.Label(self.left_frame, text="时").grid(row=0, column=7, sticky="w")
        tk.Entry(self.left_frame, textvariable=self.min_var, width=3).grid(row=0, column=8)
        tk.Label(self.left_frame, text="分").grid(row=0, column=9, sticky="w")
        tk.Entry(self.left_frame, textvariable=self.sec_var, width=3).grid(row=0, column=10)
        tk.Label(self.left_frame, text="秒").grid(row=0, column=11, sticky="w")
        tk.Button(self.left_frame, text="确认修改时间", command=self.confirm_set_time).grid(row=1, column=0,
                                                                                            columnspan=12, pady=5)

        # 右侧：恢复时间
        tk.Button(self.right_frame, text="恢复时间", command=self.restore_time).grid(row=1, column=0, pady=10)

        # 底部提示文字
        tk.Label(self, text="理论启动服务端和启动器后不退出\n【不用】【断网】和【改时间】-【可退游】",
                 font=('Microsoft YaHei', 14, 'bold'), fg='#B700FF', anchor='center').grid(row=3, column=0,
                                                                                           columnspan=3, pady=10,
                                                                                           sticky="ew")

    def browse_program(self):
        path = filedialog.askopenfilename(title="选择要运行的程序",
                                          filetypes=[("可执行文件", "*.exe"), ("所有文件", "*.*")])
        if path:
            self.program_path.set(path)

    def get_system_time(self):
        class SYSTEMTIME(ctypes.Structure):
            _fields_ = [
                ("wYear", ctypes.c_uint16),
                ("wMonth", ctypes.c_uint16),
                ("wDayOfWeek", ctypes.c_uint16),
                ("wDay", ctypes.c_uint16),
                ("wHour", ctypes.c_uint16),
                ("wMinute", ctypes.c_uint16),
                ("wSecond", ctypes.c_uint16),
                ("wMilliseconds", ctypes.c_uint16),
            ]

        st = SYSTEMTIME()
        ctypes.windll.kernel32.GetLocalTime(ctypes.byref(st))  # 使用本地时间（北京时间）
        return (st.wYear, st.wMonth, st.wDay, st.wHour, st.wMinute, st.wSecond, st.wMilliseconds)

    def set_system_time(self, year, month, day, hour=0, min=0, sec=0, ms=0):
        class SYSTEMTIME(ctypes.Structure):
            _fields_ = [
                ("wYear", ctypes.c_uint16),
                ("wMonth", ctypes.c_uint16),
                ("wDayOfWeek", ctypes.c_uint16),
                ("wDay", ctypes.c_uint16),
                ("wHour", ctypes.c_uint16),
                ("wMinute", ctypes.c_uint16),
                ("wSecond", ctypes.c_uint16),
                ("wMilliseconds", ctypes.c_uint16),
            ]

        st = SYSTEMTIME()
        st.wYear = year
        st.wMonth = month
        st.wDay = day
        st.wHour = hour
        st.wMinute = min
        st.wSecond = sec
        st.wMilliseconds = ms
        st.wDayOfWeek = 0
        ctypes.windll.kernel32.SetLocalTime(ctypes.byref(st))  # 使用本地时间（北京时间）

    def sync_windows_time(self):
        """使用 NTP 库直接同步系统时间到北京时间"""
        try:
            client = ntplib.NTPClient()
            response = client.request('ntp.aliyun.com', version=3, timeout=5)  # 使用阿里云 NTP 服务器
            ntp_time = datetime.fromtimestamp(response.tx_time)  # 转换为北京时间
            # 设置系统时间
            self.set_system_time(ntp_time.year, ntp_time.month, ntp_time.day, ntp_time.hour, ntp_time.minute, ntp_time.second)
            return ntp_time
        except Exception as e:
            print(f"NTP 同步失败: {e}")
            return False

    def launch_program(self):
        """仅启动程序，不修改时间"""
        if not self.program_path.get():
            messagebox.showerror("错误", "请先选择程序")
            return
        # 直接启动程序
        subprocess.Popen([self.program_path.get()])
        # messagebox.showinfo("提示", "程序已启动")

    def confirm_set_time(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
            day = int(self.day_var.get())
            hour = int(self.hour_var.get())
            min = int(self.min_var.get())
            sec = int(self.sec_var.get())
            # 设置系统时间
            self.set_system_time(year, month, day, hour, min, sec)
            messagebox.showinfo("完成", "时间已修改为：{}-{}-{} {}:{}:{}".format(year, month, day, hour, min, sec))
        except Exception as e:
            messagebox.showerror("错误", "设置时间时发生错误：{}".format(e))

    def restore_time(self):
        if messagebox.askokcancel("提示", "网络开了吗就点，同步网络时间"):
            success = self.sync_windows_time()
            if success:
                messagebox.showinfo("完成", f"时间已同步到最新北京时间\n设置时间: {success.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                messagebox.showwarning("警告", "同步失败，请检查网络")


if __name__ == "__main__":
    app = GameConditionLauncher()
    app.mainloop()

