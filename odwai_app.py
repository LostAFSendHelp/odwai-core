import wx
import wx.adv

from odwai_window import OdwaiWindow

TRAY_TOOLTIP = "ODWai"
TRAY_ICON = "icon.png"


# Tạo option trên menu chuột phải của tray icon
def create_menu_item(menu, label, function):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, function, id=item.GetId())
    menu.Append(item)
    return item

# Class tạo app chạy trên tray
class TaskBarIcon(wx.adv.TaskBarIcon):
    
    # khởi tạo
    def __init__(self, frame, master):
        self.frame = frame
        
        # khởi tạo lớp cha
        super(TaskBarIcon, self).__init__()

        # gán icon sẽ hiển thị trên tray
        self.set_icon(TRAY_ICON)

        # gán sự kiện: chuột trái lên biểu tượng trên tray
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)
        
        # gán thuộc tính master
        self.master = master

        # bỏ qua check kết quả bằng hình ảnh
        self.skip_check = master.skip_check
        
        # khởi tạo window GUI, truyền self để window gọi lại hàm
        self.window = OdwaiWindow(self)

        # gọi on_leftdown để hiện thị window
        self.on_left_down(wx.adv.EVT_TASKBAR_LEFT_DOWN)

    def CreatePopupMenu(self):
        # tạo menu
        menu = wx.Menu()

        # tạo các option
        create_menu_item(menu, "Get\tCtrl + f1", self.on_get)
        create_menu_item(menu, "Static\tCtrl + f2", self.on_static)
        create_menu_item(menu, "Realtime\tCtrl + f3", self.on_realtime)
        create_menu_item(menu, "Automate\tCtrl + f6", self.on_simulate)
        
        # tạo separator
        menu.AppendSeparator()
        create_menu_item(menu, "Exit\tCtrl + Q", self.on_exit)

        return menu

    # gán icon theo đường dẫn
    def set_icon(self, path):
        icon = wx.Icon(path)
        self.SetIcon(icon, TRAY_TOOLTIP)

    # sự kiện left click lên tray icon
    def on_left_down(self, event):
        self.window.Show()

    # sự kiện đóng window
    def on_window_close(self, event=None):
        self.window.Hide()

    # sự kiện get custom frame, gọi hàm thông qua master
    def on_get(self, event=None):
        self.master.btnGetClick()

    # sự kiện nhận diện thời gian thực
    def on_realtime(self, event=None):
        self.master.callRealtime()

    # sự kiện nhận diện 1 khung hình, gọi hàm thông qua master
    def on_static(self, event=None):
        self.master.callCapture()

    # sự kiện mô automate/mô phỏng user input
    def on_simulate(self, event=None):
        self.master.callTbSimulate()

    # sự kiện toggle skip kiểm tra kết quả bằng hình ảnh
    def toggle_skip_check(self, event=None):
        self.skip_check = not self.skip_check
        self.master.skip_check = self.skip_check

    # sự kiện thoát ứng dụng
    def on_exit(self, event=None):
        self.frame.Destroy()
        self.window.Destroy()
        self.Destroy()
