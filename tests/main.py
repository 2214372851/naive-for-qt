from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os
from src import NCore, NUtils, NView
from functools import partial


class AvatarPage(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setLayout(NView.BashVBoxLayout())
        self.dimension()
        self.shape()
        self.text()
        self.layout().setSpacing(5)
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def dimension(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('头像有 small、medium 和 large 大小，也可以自己设定尺寸。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Avatar(icon=QtGui.QImage('07akioni.jpeg'), size=NCore.Core.Size.small)
        )
        show_widget.layout().addWidget(
            NView.Avatar(icon=QtGui.QImage('07akioni.jpeg'), size=NCore.Core.Size.medium)
        )
        show_widget.layout().addWidget(
            NView.Avatar(icon=QtGui.QImage('07akioni.jpeg'), size=NCore.Core.Size.large)
        )
        show_widget.layout().addWidget(
            NView.Avatar(icon=QtGui.QImage('07akioni.jpeg'), size=50)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='尺寸',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def shape(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('头像可以是圆形。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Avatar(
                icon=QtGui.QImage('07akioni.jpeg'),
                size=NCore.Core.Size.small,
                circle=NCore.Core.Switch.on,
                background=(204, 204, 204, 255)
            )
        )
        show_widget.layout().addWidget(
            NView.Avatar(
                icon=QtGui.QImage('07akioni.jpeg'),
                size=NCore.Core.Size.medium,
                circle=NCore.Core.Switch.on,
                background=(204, 204, 204, 255)
            )
        )
        show_widget.layout().addWidget(
            NView.Avatar(
                icon=QtGui.QImage('07akioni.jpeg'),
                size=NCore.Core.Size.large,
                circle=NCore.Core.Switch.on,
                background=(204, 204, 204, 255)
            )
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='形状',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def text(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('头像可以是圆形。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Avatar(
                icon='图',
                size=NCore.Core.Size.medium,
                background=(101, 190, 236, 255)
            )
        )
        show_widget.layout().addWidget(
            NView.Avatar(
                icon='好',
                size=NCore.Core.Size.medium,
                circle=NCore.Core.Switch.on,
                background=(101, 190, 236, 255),
            )
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='形状',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)


class ButtonPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setLayout(NView.BashVBoxLayout())
        self.basics()
        self.secondary()
        self.tertiary()
        self.dashed()
        self.dimension()
        self.text()
        self.layout().setSpacing(5)
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def basics(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('按钮的 type 分别为 default、tertiary、info、success、warning 和 error。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('Default')
        )
        show_widget.layout().addWidget(
            NView.Button('Tertiary', style_type=NCore.Core.ButtonType.tertiary)
        )
        show_widget.layout().addWidget(
            NView.Button('Info', style_type=NCore.Core.ButtonType.info)
        )
        show_widget.layout().addWidget(
            NView.Button('Success', style_type=NCore.Core.ButtonType.success)
        )
        show_widget.layout().addWidget(
            NView.Button('Warning', style_type=NCore.Core.ButtonType.warning)
        )
        show_widget.layout().addWidget(
            NView.Button('Error', style_type=NCore.Core.ButtonType.error)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='基础',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def secondary(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        # info = QtWidgets.QLabel('按钮的 type 分别为 default、tertiary、info、success、warning 和 error。')
        # info.setWordWrap(True)
        # info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('Default', style_type=NCore.Core.ButtonType.secondary_default)
        )
        show_widget.layout().addWidget(
            NView.Button('Tertiary', style_type=NCore.Core.ButtonType.secondary_tertiary)
        )
        show_widget.layout().addWidget(
            NView.Button('Info', style_type=NCore.Core.ButtonType.secondary_info)
        )
        show_widget.layout().addWidget(
            NView.Button('Success', style_type=NCore.Core.ButtonType.secondary_success)
        )
        show_widget.layout().addWidget(
            NView.Button('Warning', style_type=NCore.Core.ButtonType.secondary_warning)
        )
        show_widget.layout().addWidget(
            NView.Button('Error', style_type=NCore.Core.ButtonType.secondary_error, round=NCore.Core.Switch.on)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='次要按钮',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def tertiary(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        # info = QtWidgets.QLabel('按钮的 type 分别为 default、tertiary、info、success、warning 和 error。')
        # info.setWordWrap(True)
        # info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('Default', style_type=NCore.Core.ButtonType.tertiary_default)
        )
        show_widget.layout().addWidget(
            NView.Button('Tertiary', style_type=NCore.Core.ButtonType.tertiary_tertiary)
        )
        show_widget.layout().addWidget(
            NView.Button('Info', style_type=NCore.Core.ButtonType.tertiary_info)
        )
        show_widget.layout().addWidget(
            NView.Button('Success', style_type=NCore.Core.ButtonType.tertiary_success)
        )
        show_widget.layout().addWidget(
            NView.Button('Warning', style_type=NCore.Core.ButtonType.tertiary_warning)
        )
        show_widget.layout().addWidget(
            NView.Button('Error', style_type=NCore.Core.ButtonType.tertiary_error, round=NCore.Core.Switch.on)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='次次要按钮',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def dashed(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('使用 dashed 来使用虚线按钮。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('Default', style_type=NCore.Core.ButtonType.dashed_default)
        )
        show_widget.layout().addWidget(
            NView.Button('Tertiary', style_type=NCore.Core.ButtonType.dashed_tertiary)
        )
        show_widget.layout().addWidget(
            NView.Button('Info', style_type=NCore.Core.ButtonType.dashed_info)
        )
        show_widget.layout().addWidget(
            NView.Button('Success', style_type=NCore.Core.ButtonType.dashed_success)
        )
        show_widget.layout().addWidget(
            NView.Button('Warning', style_type=NCore.Core.ButtonType.dashed_warning)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='虚线按钮',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def dimension(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('有 small、medium 和 large 尺寸')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('Default',
                         style_type=NCore.Core.ButtonType.dashed_default,
                         size=NCore.Core.Size.small)
        )
        show_widget.layout().addWidget(
            NView.Button('Default',
                         style_type=NCore.Core.ButtonType.dashed_default,
                         size=NCore.Core.Size.medium)
        )
        show_widget.layout().addWidget(
            NView.Button('Default',
                         style_type=NCore.Core.ButtonType.dashed_default,
                         size=NCore.Core.Size.large)
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='尺寸',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def text(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        show_widget = QtWidgets.QWidget()
        show_widget.setLayout(NView.BashHBoxLayout())
        show_widget.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        show_widget.layout().setSpacing(30)

        info = QtWidgets.QLabel('长得就像文本。')
        info.setWordWrap(True)
        info_widget.layout().addWidget(info)

        show_widget.layout().addWidget(
            NView.Button('哔哩哔哩',
                         style_type=NCore.Core.ButtonType.text,
                         size=NCore.Core.Size.medium,
                         callback=lambda: os.system("start https://www.bilibili.com/"))
        )
        info_widget.layout().addWidget(show_widget)

        card = NView.Card(
            title='文本按钮',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)


class CardPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setLayout(NView.BashVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout().setSpacing(10)
        self.basics()
        self.dimension()
        self.suspension()
        self.sockets()
        self.border()

    def basics(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        label = QtWidgets.QLabel('基础卡片')
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            NView.Card(
                title='卡片',
                content=QtWidgets.QLabel('卡片内容')
            )
        )
        card = NView.Card(
            title='基础用法',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def dimension(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())
        info_widget.layout().setSpacing(6)

        label = QtWidgets.QLabel('卡片有 small、medium、large、huge 尺寸。')
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            NView.Card(
                title='小卡片',
                content=QtWidgets.QLabel('卡片内容'),
                size=NCore.Core.Size.small
            )
        )
        info_widget.layout().addWidget(
            NView.Card(
                title='中卡片',
                content=QtWidgets.QLabel('卡片内容'),
                size=NCore.Core.Size.medium
            )
        )
        info_widget.layout().addWidget(
            NView.Card(
                title='大卡片',
                content=QtWidgets.QLabel('卡片内容'),
                size=NCore.Core.Size.large
            )
        )
        info_widget.layout().addWidget(
            NView.Card(
                title='超大卡片',
                content=QtWidgets.QLabel('卡片内容'),
                size=NCore.Core.Size.huge
            )
        )
        card = NView.Card(
            title='尺寸',
            content=info_widget
        )
        card.setFixedHeight(700)
        self.layout().addWidget(card)

    def suspension(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())
        info_widget.layout().setContentsMargins(6, 6, 6, 6)

        label = QtWidgets.QLabel('Layout 需要有 ContentsMargins，否则无法显示')
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            NView.Card(
                title='卡片',
                content=QtWidgets.QLabel('卡片内容'),
                hover=NCore.Core.Switch.on
            )
        )
        card = NView.Card(
            title='可悬浮',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)

    def sockets(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())
        info_widget.layout().setContentsMargins(6, 6, 6, 6)

        label = QtWidgets.QLabel('卡片有很多插槽，希望能帮你少写点代码。')
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            NView.Card(
                title='卡片插槽示例',
                extra=QtWidgets.QLabel('#header-extra'),
                content=QtWidgets.QLabel('卡片内容'),
                footer=QtWidgets.QLabel('#footer'),
                action=QtWidgets.QLabel('#action')
            )
        )
        card = NView.Card(
            title='插槽',
            content=info_widget
        )
        card.setFixedHeight(400)
        self.layout().addWidget(card)

    def border(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        label = QtWidgets.QLabel('卡片可以没有边框。')
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            NView.Card(
                title='无边框的卡片',
                content=QtWidgets.QLabel('卡片内容'),
                bordered=NCore.Core.Switch.off
            )
        )
        card = NView.Card(
            title='边框',
            content=info_widget
        )
        card.setFixedHeight(200)
        self.layout().addWidget(card)


class CarouselPage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setLayout(NView.BashVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.layout().setSpacing(10)
        self.basics()
        # self.dimension()
        # self.suspension()
        # self.sockets()
        # self.border()

    def basics(self):
        info_widget = QtWidgets.QWidget()
        info_widget.setLayout(NView.BashVBoxLayout())

        label = QtWidgets.QLabel('基础卡片')
        label.setFixedHeight(label.sizeHint().height() + 5)
        label.setWordWrap(True)
        info_widget.layout().addWidget(label)

        info_widget.layout().addWidget(
            # NView.Carousel(
            #     data=[
            #         NView.CarouselItem(
            #             src='1.jpg',
            #             callback=partial(os.system, 'start www.baidu.com/s?wd=金克丝')
            #         ),
            #         NView.CarouselItem(
            #             src='2.jpg',
            #             callback=partial(os.system, 'start www.baidu.com/s?wd=高达')
            #         ),
            #         NView.CarouselItem(
            #             src='3.jpg',
            #             callback=partial(os.system, 'start www.baidu.com/s?wd=王者荣耀')
            #         ),
            #         NView.CarouselItem(
            #             src='4.jpg',
            #             callback=partial(os.system, 'start www.baidu.com/s?wd=顾清寒')
            #         ),
            #     ],
            #     wheel=NCore.Core.Switch.on,
            #     arrow=NCore.Core.Switch.on,
            #     autoplay=NCore.Core.Switch.on
            # )
            # NView.Collapse(
            #     data=[
            #         NView.CollapseItem(
            #             title='青铜',
            #             icon='naive.svg',
            #             callback=None,
            #             child=[
            #                 NView.CollapseItem(
            #                     title='可以',
            #                     icon='naive.svg',
            #                     callback=lambda: print('可以'),
            #                     child=[]
            #                 )
            #             ]
            #         ),
            #         NView.CollapseItem(
            #             title='白银',
            #             icon='naive.svg',
            #             callback=None,
            #             child=[
            #                 NView.CollapseItem(
            #                     title='很好',
            #                     icon='naive.svg',
            #                     callback=lambda: print('很好'),
            #                     child=[]
            #                 )
            #             ]
            #         ),
            #         NView.CollapseItem(
            #             title='黄金',
            #             icon='naive.svg',
            #             callback=None,
            #             child=[
            #                 NView.CollapseWidgetItem(
            #                     widget=NView.Button('真棒的按钮', style_type=NCore.Core.ButtonType.error)
            #                 )
            #             ]
            #         ),
            #     ]
            # )
            # NView.Dropdown(text='你好', style_type=NCore.Core.ButtonType.info, menus=[
            #     NView.DropdownItem(
            #         name='一级菜单-1',
            #         icon='Icons:card-two.svg',
            #         children=[
            #             NView.DropdownItem(
            #                 name='二级菜单',
            #                 icon='Icons:naive.svg',
            #                 callback=lambda: print('二级')
            #             )
            #         ]
            #     )
            # ])
            NView.Text('h1 标签')
        )
        card = NView.Card(
            title='基础',
            content=info_widget
        )
        card.setFixedHeight(400)
        self.layout().addWidget(card)


class TestWindow(NView.MainWindow):

    def __init__(self):
        menus = [
            NView.MenuItem(
                title='Carousel',
                icon='Icons:card-two.svg',
                page=NView.Scroll(CarouselPage()),
                callback=None
            ),
            NView.MenuItem(
                title='Card',
                icon='Icons:card-two.svg',
                page=NView.Scroll(CardPage()),
                callback=None
            ),
            NView.MenuItem(
                title='Button',
                icon='Icons:view-grid-card.svg',
                page=NView.Scroll(ButtonPage()),
                callback=None
            ),
            NView.MenuItem(
                title='Avatar',
                icon='Icons:avatar.svg',
                page=NView.Scroll(AvatarPage()),
                callback=None
            ),
        ]
        super().__init__(
            title='Test Naive Ui',
            version='preview',
            icon='Icons:naive.svg',
            menus=menus
        )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TestWindow()
    window.show()
    with open(r'../src\Naive\static\light.css', 'r', encoding='utf-8') as f:
        a = f.read()
        app.setStyleSheet(a)
    sys.exit(app.exec())
