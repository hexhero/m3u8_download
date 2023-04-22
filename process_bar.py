# 进度条函数
def progress_bar(current, total):
    percent = current / total  # 完成百分比
    bar_num = int(percent * 50)  # 计算进度条的长度

    # 格式化输出进度条
    print('\r', '[', '▋'*bar_num, ' '*(50-bar_num), ']', f'{percent:.0%} [{current}/{total}]', end='', flush=True)

# # 模拟进度
# for i in range(101):
#     progress_bar(i, 100)
#     time.sleep(0.05)  # 模拟耗时操作