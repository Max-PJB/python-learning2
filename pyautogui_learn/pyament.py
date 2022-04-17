import pyautogui  # https://pyautogui.readthedocs.io/en/latest/mouse.html
import keyboard  # 监听键盘
import mouse  # 监听鼠标  https://github.com/boppreh/mouse


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)


def get_click_pos():
    x, y = pyautogui.position()
    positionStr = '鼠标坐标点（X,Y）为：{},{}'.format(str(x).rjust(4), str(y).rjust(4))
    print(positionStr)


# key_in = input()
# if key_in == 'p':
#     get_click_pos()


def test_a():
    print('aaa')


def test(x):
    print(x)


if __name__ == '__main__':
    mouse.on_click(get_click_pos)
    keyboard.add_hotkey('c', test_a)
    # 按c输出aaa
    keyboard.add_hotkey('d', test, args=('b',))
    # 按d输出b
    keyboard.wait()
    # wait里也可以设置按键，说明当按到该键时结束
