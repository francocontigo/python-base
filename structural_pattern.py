# Python 3.10 +
# Structural Pattern Matching

print(
    """\
    Jogo da Tartaruga

    comandos:
        move x y
        move steps
        turn angle (default 90)
        draw shape size (line | circle)
        write text
        stop | exit | quit
    """
)

from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("yellow", "green")
turtle.penup()

while True:
    command: list[str] = input("🐢>").strip().split()
    # semelhante a switch - case, no python é estrutual, se preocupa com a estrutura e não com valores
    match command:  # target

        case ["move", *points]:
            match points:
                case [x, y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))

        case ["turn", *angle]:
            match angle:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)

        case ["draw", shape, size]:
            turtle.pendown()
            match shape:
                case "circle":
                    turtle.circle(float(size))
                case "line":
                    turtle.forward(float(size))
            turtle.penup()

        case ["write", *text]:
            turtle.write(" ".join(text), None, "Center", "16pt 20")

        case ["stop" | "exit" | "quit"]:
            break
        case _:
            print("Invalid command")
