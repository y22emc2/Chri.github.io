import turtle
import turtle as t
import random as r
word = "给静静的圣诞树🎄"  # 写字
def writes1():       #写字：“圣诞快乐!”
    t.pencolor("cyan")      #画笔颜色，天蓝色
    t.hideturtle()          #隐藏画笔
    t.up()
    t.goto(-180, 240)      #从（0，240）开始写字
    t.down()
    t.pencolor("pink")
    t.write(word, font=("Comic Sans MS", 40, "bold"))
def star():     #画圣诞树顶的大星星
    t.hideturtle()      #隐藏画笔
    t.pensize(2)        #给画笔设置大小
    t.pencolor("gold")  #给画笔设置颜色，'gold'表示金色
    t.up()              #提起画笔，画笔移动时不会画画
    t.forward(5)        #将画笔向前移5个像素（此时画笔方向向右，即向右移动5个像素）
    t.down()            #画笔放下，画笔移动时会产生轨迹
    t.begin_fill()      #给星星填充颜色
    for i in range(5):  #因为是五角星，所以要循环五次画五个角
        t.forward(20)
        t.right(144)
        t.forward(20)
        t.left(72)
    t.fillcolor('yellow')   #设置填充的颜色
    t.end_fill()
    return
def stars():          #画圣诞树上的小星星
    t.hideturtle()       #隐藏画笔
    t.speed(0)           #设置画画速度，0为最快速
    t.pensize(5)         #设置画笔大小
    for i in range(5):   #循环五次画五个角，与画大星星一样
        t.forward(5)
        t.right(144)
        t.forward(5)
        t.left(72)
    return
def stares():           #循环画圣诞树上的小星星
    t.hideturtle()      #隐藏画笔
    x1=-110   #x1赋初值
    x2=110    #x2赋初值
    y1=-40    #y1赋初值
    y2=-15    #y2赋初值
    n=0       #n用来控制在圣诞树两边画星星
    c = ['red', 'orange', 'yellow', 'brown', 'cyan', 'pink', 'blue', 'blueviolet','gold','white']    #星星的颜色，可自定义
    for i in c:   #循环画不同颜色的星星
        t.pencolor(i)     #每次从颜色列表c中按序取一个颜色
        t.up()      #找画星星的位置时要记得提起画笔
        if n%2==0:        #当n为偶数时在圣诞树左边画星星
            t.setx(r.randint(x1,0))
            t.sety(r.randint(y1,y2))
        else:             #当n为奇数时在圣诞树右边画星星
            t.setx(r.randint(0,x2))
            t.sety(r.randint(y1,y2))
        t.down()
        stars()     #开始画星星
        x1+=10      #每次画完记得按圣诞树的层数要将x1,x2减小，y1,y2上移
        x2-=10
        y1+=25
        y2+=25
        n+=1        #n=n+1
def tree(d,s):      #运用递归的方法画圣诞树
    t.hideturtle()              #隐藏画笔
    t.pencolor('limegreen')     #画笔颜色置为绿色，用来画树
    t.pensize(5)                #画笔大小为5
    t.speed(0)                  #最快速度画树（其实挺慢的）
    if d<=0:
        return
    t.forward(s)
    tree(d-1,s*0.8)
    t.right(120)
    tree(d-3,s*0.5)
    t.right(120)
    tree(d-3,s*0.5)
    t.right(120)
    t.backward(s)
def trees():          #画完整的圣诞树
    t.hideturtle()          #隐藏画笔
    t.left(90)              #将画笔向左旋转90度
    t.up()                  #提起画笔
    t.goto(0,-110)          #移动画笔到坐标（0，-110）处开始画树
    t.down()
    t.pencolor('saddlebrown')   #先画树根，将画笔置为棕色
    t.pensize(20)           #树根比较粗，画笔大小设置大一点
    t.forward(50)           #树根长度为50个像素
    t.up()                  #提笔
    t.goto(0,-50)           #将画笔移到（0，-50）处
    t.down()
    tree(15,60)             #调用画树的递归函数，慢慢画树
    t.goto(0,250)           #画完树后，将画笔移到（0，250）的位置，准备画大星星
    t.down()
    t.right(90)             #将画笔向右旋转90度，指向右方，准备画大星星
    star()                  #画大星星
def snow():            #画雪花（全屏）
    t.hideturtle()     #隐藏画笔
    t.pensize(2)       #画笔大小
    t.speed(0)         #画雪花的速度
    for i in range(500):          #循环画500个雪花
        t.pencolor('white')       #雪花是白色的
        t.penup()                 #提笔
        t.setx(r.randint(-1000,1000))     #在画布上随机找点
        t.sety(r.randint(-1000,1000))
        t.pendown()
        snowsize=r.randint(4,10)          #雪花大小
        for i in range(6):            #画雪花（雪花为六瓣，需要循环六次）
            t.forward(int(snowsize))
            t.backward(int(snowsize))
            t.left(60)
def gift():       #画正方体礼物盒
    t.hideturtle()       #隐藏画笔
    t.speed(0)           #画笔速度
    x=40    #礼物盒的长和宽，我设置为正方形礼物盒，长宽高相等
    y=16    #由于是立体图形，宽与长不一样
    for i in range(4):    #以下为画礼物盒的方法（x,y的值可以自行修改）
        t.forward(x)
        t.left(90)
    t.up()
    t.left(45)
    t.forward(y)
    t.right(45)
    t.down()
    for i in range(4):
        t.forward(x)
        t.left(90)
    t.up()
    t.right(135)
    t.forward(y)
    t.down()
    t.left(180)
    t.forward(y)
    t.backward(y)
    t.right(45)
    t.forward(x)
    t.left(45)
    t.forward(y)
    t.backward(y)
    t.left(45)
    t.forward(x)
    t.right(45)
    t.forward(y)
    t.backward(y)
    t.left(135)
    t.forward(x)
    t.right(135)
    t.forward(y)
    t.backward(y)
    t.right(135)
    t.forward(x)
    t.left(90)
def gifts():            #画多个正方体礼物盒
    t.hideturtle()      #隐藏画笔
    t.penup()           #提笔
    t.goto(-180,-150)    #将画笔移到（-180，-150）的位置准备画礼物盒
    t.pendown()
    t.pensize(5)         #画笔大小
    c=['red','orange','yellow','green','cyan','blue','blueviolet']    #礼物盒的颜色
    for i in c:          #循环画不同颜色的礼物盒
        t.up()
        t.forward(40)
        t.down()
        t.pencolor(i)
        gift()
def writes():       #写字：“圣诞快乐!”
    t.pencolor("cyan")      #画笔颜色，天蓝色
    t.hideturtle()          #隐藏画笔
    t.up()
    t.goto(-160,-250)       #从（-160，-250）开始写字
    t.down()
    t.write("Merry Christmas!",font=("Comic Sans MS",30,"bold"))   #开始写字，"Merry Christmas!"为要写的字，"Comic Sans MS"为字体，30为字的大小，bold为粗体（可自行修改要写的字）
def treet(d,s):      #运用递归的方法画圣诞树
    t.hideturtle()              #隐藏画笔
    t.pencolor('limegreen')     #画笔颜色置为绿色，用来画树
    t.pensize(5)                #画笔大小为5
    t.speed(0)                  #最快速度画树（其实挺慢的）
    if d<=0:
        return
    t.forward(s)
    treet(d-1,s*0.8)
    t.right(120)
    treet(d-3,s*0.5)
    t.right(120)
    treet(d-3,s*0.5)
    t.right(120)
    t.backward(s)
if __name__ == '__main__':      #主函数
    '''
    t.bgcolor('black')
    t.up()
    t.goto(0,-110)
    t.down()
    t.left(90)
    treet(10,60)
    t.done()
    '''
    turtle.bgcolor("black")
    turtle.setup(1.0,1.0)
    turtle.title("圣诞树（2023）")
    # turtle.tracer(0)   #直接画完
    t = turtle.Turtle()
    t.screen.delay(0)    #加速画
    writes1()
    trees()         #画圣诞树
    stares()        #画树上的星星
    gifts()         #画礼物盒
    writes()        #写祝福语
    snow()          #下雪（画雪花）
    turtle.mainloop()        #将画板停住（否则画完画会自动退出画画界面）
