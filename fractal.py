# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui as Qg, QtWidgets as Qw, QtCore as Qt
from multiprocessing import Pool
import fractal_form  # デザイナーで作った画面をインポートする
import param_form
import numpy as np
import time


def mandel_multi(para):
    """
    発散判定をマルチプロセスで行う
    [0:500]:1行分の計算結果
    [-1]:発散基準
    [-2]:最大計算回数
    """
    x = para
    c = x[0:500]
    dg = int(x[-1].real)
    cn = int(x[-2].real)
    # zの複素数を生成
    z = np.zeros(c.shape, dtype=complex)
    # インデックスを描画する座標、要素を色とする配列を生成
    index = np.zeros(c.shape, dtype=int)
    for k in range(cn):
        mask = np.less(np.abs(z), dg)
        index[mask] = k
        z[mask] = np.add(np.power(z[mask], 2), c[mask])

    # 最後まで発散しなかったインデックスはこれに該当する(例えば中央付近)
    # パレットを作る際に末尾に発散しない座標用の色を用意しているのでcnを代入
    index[index == cn - 1] = cn
    return index


def julia_multi(para):
    """
    発散判定をマルチプロセスで行う
    [0:500]:1行分の計算結果
    [-1]:複素数Cの値
    [-2]:発散基準
    [-3]:最大計算回数
    """
    x = para
    z = x[0:500]
    c = x[-1]
    dg = int(x[-2].real)
    cn = int(x[-3].real)
    index = np.zeros(z.shape, dtype=int)
    for k in range(cn):
        mask = np.less(np.abs(z), dg)
        index[mask] = k
        z[mask] = np.add(np.power(z[mask], 2), c)

    index[index == cn - 1] = cn
    return index


class MyForm(Qw.QMainWindow):
    def __init__(self, parent=None):
        """
        各変数の初期化を行う
        """
        super().__init__(parent)
        self.ui = fractal_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.pix = self.ui.graphicsView.width()
        self.img = Qg.QImage(self.pix, self.pix, Qg.QImage.Format_ARGB32)
        self.canvas = self.make_canvas(self.img, self.pix)
        self.canvas.translate(self.pix / 2, self.pix / 2)  # キャンバスの中央を原点とする
        self.canvas.scale(1, -1)  # y軸反転
        self.index = np.array((500, 500))

        # カラーパレットに関する変数
        self.colortable = []
        self.hstart = 100
        self.s = 255

        # どちらの集合を描いたかのフラグ
        self.drawflag = 0

        # 一つ前に中心として指定された座標
        self.pre_x = 0
        self.pre_y = 0

        # 発散を判定する際の計算回数
        self.mCalcNum = 30
        self.jCalcNum = 700

        # 発散するかどうかの判定基準
        self.mdg = 2
        self.jdg = 2

        # 拡大率(4がデフォルト.小さくすると拡大される)
        self.mScale = 4
        self.jScale = 4

        # 中心の座標
        self.mCenter_x = 0
        self.mCenter_y = 0
        self.jCenter_x = 0
        self.jCenter_y = 0

        # ジュリア集合におけるCの実部と虚部
        self.real_num = -0.8
        self.im_num = 0.156

        # ディスプレイの解像度とウィンドウのサイズを取得
        res = Qw.qApp.desktop()
        fsize = self.size()

        # パラメータを設定するウィンドウを表示する
        # 表示する際にウィンドウが重ならないように移動させる
        self.param_window = ParamWindow(self)
        self.param_window.move(int((res.width() + fsize.width()) / 2 + 10),
                               int((res.height() - fsize.height()) / 2 - 30))
        self.param_window.show()

    def calc_mandel(self, scale, px, cx, cy, cn, dg):
        """
        マンデルブロ集合の計算に用いる各座標の複素数Cを用意する
        """
        st = time.time()
        x = []
        pl = []
        for i in range(px):
            x.append((1 / 125 * i - 2) * scale / 4 + cx)

        nx = np.array(x, dtype=float)

        for j in range(px):
            a = nx + ((1 / 125 * j - 2) *
                      scale / 4 + (-cy)) * 1j
            pl.append(np.append(a, [cn, dg]))  # １行毎のパラメータ

        with Pool() as p:
            result = p.map(mandel_multi, pl)

        index = np.array(result, dtype=int)
        print(time.time() - st)
        return index.T

    # ジュリア集合に属する点を求める
    def calc_julia(self, scale, px, cx, cy, cn, dg):
        """
        ジュリア集合の計算に用いる各座標の複素数zを用意する
        """
        c = complex(self.real_num, self.im_num)  # ここを変化させると図形が変わる
        x = []
        pl = []
        core = 4
        for i in range(px):
            x.append((1 / 125 * i - 2) * scale / 4 + cx)

        nx = np.array(x, dtype=float)

        for j in range(px):
            a = nx + ((1 / 125 * j - 2) *
                      scale / 4 + (-cy)) * 1j
            pl.append(np.append(a, [cn, dg, c]))  # １行毎のパラメータ

        with Pool(core) as p:
            result = p.map(julia_multi, pl)

        index = np.array(result, dtype=int)
        return index.T

    def draw_fractal(self, canvas, index, ct):
        """
        計算で求めた座標を元に描画していく
        """
        # iには座標、clには色番号を与える
        for i, cl in np.ndenumerate(index):
            canvas.setPen(ct[cl])
            canvas.drawPoint(float(i[0] - self.pix / 2),
                             float(-i[1] + self.pix / 2))

    def redraw(self):
        self.draw_fractal(self.canvas, self.index, self.colortable)
        self.make_scene(self.img)

    def closeEvent(self, event):
        """
        描画ウィンドウが閉じられたときパラメータウィンドウも閉じる
        """
        self.param_window.close()

    def make_canvas(self, img, w):
        """
        キャンバスの作成
        """
        canvas = Qg.QPainter(img)  # self.imgにお絵かきできるように
        canvas.setBrush(Qg.QColor(250, 250, 250))
        canvas.drawRect(0, 0, w, w)  # ブラシ色で背景塗りつぶし
        return canvas

    def make_scene(self, img):
        """
        graphicViewオブジェクトにイメージを描画するための処理
        graphicsViewの上にシーン、シーンの上にアイテム
        """
        scene = Qw.QGraphicsScene()  # シーンを作成

        # アイテム(QPainterがself.imgにお絵かきしたものをアイテムにする)
        item = Qw.QGraphicsPixmapItem(Qg.QPixmap(img))

        scene.addItem(item)  # 作ったアイテムをシーンにのせる
        self.ui.graphicsView.setScene(scene)  # 更にシーンをViewにのせて完成

    # ここからボタンイベント
    def draw_mandel(self):
        """
        マンデルブロ集合を描画するための各種処理を呼び出す
        """
        st = time.time()
        self.param_window.confirm_mandel_param()
        self.param_window.make_palette(self.mCalcNum, self.hstart, self.s)
        self.index = self.calc_mandel(self.mScale, self.pix, self.mCenter_x,
                                      self.mCenter_y, self.mCalcNum, self.mdg)
        self.draw_fractal(self.canvas, self.index, self.colortable)
        self.pre_x = self.mCenter_x
        self.pre_y = -self.mCenter_y
        self.make_scene(self.img)
        self.drawflag = 1  # マンデルブロ集合を描いたことを示す
        et = time.time() - st
        print(et)

    # ジュリア集合を描画する
    def draw_julia(self):
        self.param_window.confirm_julia_param()
        self.param_window.make_palette(self.jCalcNum, self.hstart, self.s)
        self.index = self.calc_julia(self.jScale, self.pix,
                                     self.jCenter_x, self.jCenter_y,
                                     self.jCalcNum, self.mdg)
        self.draw_fractal(self.canvas, self.index, self.colortable)
        self.pre_x = self.jCenter_x
        self.pre_y = -self.jCenter_y
        self.make_scene(self.img)
        self.drawflag = 2  # ジュリア集合を描いたことを示す

    # 出来上がった図形をpngで保存する
    def save_Image(self):
        # 第二引数はダイアログのタイトル。第三は表示するパス
        fname = Qw.QFileDialog.getSaveFileName(self, '保存',
                                               './image', 'PNG(*.png)')
        if fname[0]:  # ファイルのパス
            self.ui.graphicsView.grab().save(fname[0])

    # 保存された図形を読み込んで表示する
    def load_Image(self):
        fname = Qw.QFileDialog.getOpenFileName(self, '開く',
                                               './image', 'PNG(*.png)')
        if fname[0]:
            self.img = Qg.QImage(fname[0])
            self.make_scene(self.img)

    # キャンバス上をクリックするとパラメータウィンドウの中心の座標がクリックしたポイントになる
    def mousePressEvent(self, mouseevent):
        # クリックした座標に拡大率、一つ前の中心を加味して新たな中心座標を求める
        if self.drawflag == 1:  # マンデルブロ集合が描かれているとき
            x = (1 / 125 * mouseevent.x() - 2) * \
                self.mScale / 4 + self.pre_x
            y = (1 / 125 * (mouseevent.y() - 54) - 2) * \
                self.mScale / 4 + self.pre_y

            self.param_window.ui.mPosXText.setText(str(x))
            self.param_window.ui.mPosYText.setText(str(y * -1))

        elif self.drawflag == 2:  # ジュリア集合が描かれているとき
            x = (1 / 125 * mouseevent.x() - 2) * \
                self.jScale / 4 + self.pre_x
            y = (1 / 125 * (mouseevent.y() - 54) - 2) * \
                self.jScale / 4 + self.pre_y

            self.param_window.ui.jPosXText.setText(str(x))
            self.param_window.ui.jPosYText.setText(str(y * -1))


# パラメータ用のウィンドウ
# 本当はサブウィンドウとして生成したかったが上手くいかないのでメインウィンドウとして生成。
class ParamWindow(Qw.QMainWindow):
    def __init__(self, parent_window, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.ui = param_form.Ui_SubWindow()
        self.setWindowFlags(Qt.Qt.Window |
                            Qt.Qt.WindowTitleHint)
        self.ui.setupUi(self)
        self.pwin = parent_window
        self.clbar_w = self.ui.colorbar.width()
        self.clbar_h = self.ui.colorbar.height()
        self.color_img = Qg.QImage(self.clbar_w, self.clbar_h,
                                   Qg.QImage.Format_ARGB32)
        self.color_canvas = self.pwin.make_canvas(self.color_img,
                                                  self.clbar_w)
        self.interval = self.clbar_w // self.pwin.mCalcNum + 1
        self.limit = self.pwin.mCalcNum + 1

    # マンデルブロ集合のパラメータを確定する
    def confirm_mandel_param(self):
        self.pwin.mCalcNum = int(self.ui.mCalcLimitText.text())
        self.pwin.mdg = int(self.ui.mdgText.text())
        self.pwin.mScale = float(self.ui.mSizeText.text())
        self.pwin.mCenter_x = float(self.ui.mPosXText.text())
        self.pwin.mCenter_y = float(self.ui.mPosYText.text())
        self.set_interval(self.pwin.mCalcNum)

    # ジュリア集合のパラメータを確定する
    def confirm_julia_param(self):
        self.pwin.jCalcNum = int(self.ui.jCalcLimitText.text())
        self.pwin.jdg = int(self.ui.jdgText.text())
        self.pwin.jScale = float(self.ui.jSizeText.text())
        self.pwin.jCenter_x = float(self.ui.jPosXText.text())
        self.pwin.jCenter_y = float(self.ui.jPosYText.text())
        self.pwin.real_num = float(self.ui.realText.text())
        self.pwin.im_num = float(self.ui.imText.text())
        self.set_interval(self.pwin.jCalcNum)

    # スライダーを調節したとき
    def move_slider(self, value):
        if self.sender() == self.ui.chromaSlider:
            self.ui.chromaText.setText(str(value))
            self.pwin.s = value
        elif self.sender() == self.ui.hueSlider:
            self.ui.hueText.setText(str(value))
            self.pwin.hstart = value

        self.make_palette(self.limit,
                          self.pwin.hstart, self.pwin.s)
        nc = 0
        for i in range(self.clbar_w):
            if i % self.interval < 1:
                self.color_canvas.fillRect(i, 0, self.interval,
                                           30, self.pwin.colortable[nc])
                nc += 1

        # シーンを作成してGraphicsViewに乗せる
        scene = Qw.QGraphicsScene()
        item = Qw.QGraphicsPixmapItem(Qg.QPixmap(self.color_img))
        scene.addItem(item)
        self.ui.colorbar.setScene(scene)

    # パレットを作成する
    def make_palette(self, climit, hstart, s):
        hc = 360  # 1周
        self.pwin.colortable = []
        for i in range(climit):
            h = (i + hstart) % hc
            if self.ui.brightBox.checkState() == Qt.Qt.Checked:
                v = 255 - (255 * i // climit)
            else:
                v = 255
            c = Qg.QColor()
            c.setHsv(h, s, v)
            self.pwin.colortable.append(c)

        self.pwin.colortable.append(Qg.QColor(255, 255, 255))

    def chenge_color(self):
        self.pwin.redraw()

    # 何色用意するか、その際にカラーバーにどのくらいの間隔で塗るか
    def set_interval(self, limit):
        self.limit = limit
        self.interval = self.clbar_w // self.limit + 1


if __name__ == '__main__':
    app = Qw.QApplication(sys.argv)  # パラメータは正しくはコマンドライン引数を与える
    wmain = MyForm()  # MyFormのインスタンスを作って
    wmain.show()  # 表示する
    sys.exit(app.exec())
