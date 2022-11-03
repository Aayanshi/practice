import turtle
aainatree = turtle.Turtle()
aainatree.screen.bgcolor("black")
aainatree.pensize(2)
aainatree.color("green")
aainatree.left(90)
aainatree.backward(100)
aainatree.speed(20000)
aainatree.shape("turtle")


def cutu_tree(i):
    if i<10:
        return
    else:
        aainatree.forward(i)
        aainatree.color("orange")
        aainatree.circle(2)
        aainatree.color("brown")
        aainatree.left(30)
        cutu_tree(3*i/4)
        aainatree.right(60)
        cutu_tree(3*i/4)
        aainatree.left(30)
        aainatree.backward(i)







cutu_tree(100)
turtle.done()
