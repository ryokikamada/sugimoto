import CHaser
import random

def main():
    value = []
    client = CHaser.Client()

    blank = 0
    enemy = 1
    block = 2
    item  = 3

    UP    = 1
    LEFT  = 3
    RIGHT = 5
    DOWN  = 7
    UPLEFT = 0
    UPRIGHT = 2
    DOWNLEFT = 6
    DOWNRIGHT = 8

    NORTH = 0   # NORTH:ブロック（壁）にぶつかるまで、上に移動する。
    WEST  = 1   # WEST:ブロック（壁）にぶつかるまで、左に移動する。
    SOUTH = 2   # SOUTH:ブロック（壁）にぶつかるまで、下に移動する。
    EAST  = 3   # EAST:ブロック（壁）にぶつかるまで、右に移動する。
    course      = SOUTH     # 大まかな進む方向
    

    while True:
        value = client.get_ready()
        dir = random.choice([UP,LEFT,RIGHT,DOWN,1,2,3,4,5,6,7,8])

        
        if value[UP] == enemy:
            client.put_up()
        elif value[LEFT] == enemy:
            client.put_left()
        elif value[RIGHT] == enemy:
            client.put_right()
        elif value[DOWN] == enemy:
            client.put_down()

        elif value[UPLEFT] == enemy:
            client.look_up()
        elif value[UPRIGHT] == enemy:
            client.look_up()
        elif value[DOWNLEFT] == enemy:
            client.look_down()
        elif value[DOWNRIGHT] == enemy:
            client.look_down()
        
        elif value[UP] == item:
            client.walk_up()
        elif value[LEFT] == item:
            client.walk_left()
        elif value[RIGHT] == item:
            client.walk_right()
        elif value[DOWN] == item:
            client.walk_down()
        elif (value[UPLEFT] == item and value[LEFT] != block):
            client.walk_left()
        elif (value[UPLEFT] == item and value[UP] != block):
            client.walk_up()
        elif (value[UPRIGHT] == item and value[UP] != block):
            client.walk_up()
        elif (value[UPRIGHT] == item and value[RIGHT] != block):
            client.walk_right()
        elif (value[DOWNLEFT] == item and value[LEFT] != block):
            client.walk_left()
        elif (value[DOWNLEFT] == item and value[DOWN] != block):
            client.walk_down()
        elif (value[DOWNRIGHT] == item and value[RIGHT] != block):
            client.walk_right()
        elif (value[DOWNRIGHT] == item and value[DOWN] != block):
            client.walk_down()
        
        
        
        elif (value[UP] == block and value[DOWN] == block and value[RIGHT] == block and value[LEFT] == block):
            client.search_right()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[LEFT] == blank and value[RIGHT] == blank and value[DOWNLEFT] == blank and value[DOWNRIGHT] == blank and value[DOWN] != block and dir == 1):
            client.walk_down()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[LEFT] == blank and value[RIGHT] == blank and value[DOWNLEFT] == blank and value[DOWNRIGHT] == blank and value[DOWN] != block and dir == 3):
            client.walk_down()
        elif (value[LEFT] == block and value[UPLEFT] == block and value[DOWNLEFT] == block and value[UP] == blank and value[DOWN] == blank and value[DOWNRIGHT] == blank and value[UPRIGHT] == blank and value[RIGHT] != block and dir == 2):
            client.walk_right()
        elif (value[LEFT] == block and value[UPLEFT] == block and value[DOWNLEFT] == block and value[UP] == blank and value[DOWN] == blank and value[DOWNRIGHT] == blank and value[UPRIGHT] == blank and value[RIGHT] != block and dir == 1):
            client.walk_right()
        elif (value[DOWN] == block and value[DOWNLEFT] == block and value[DOWNRIGHT] == block and value[LEFT] == blank and value[RIGHT] == blank and value[UPLEFT] == blank and value[UPRIGHT] == blank and value[UP] != block and dir == 1):
            client.walk_up()
        elif (value[DOWN] == block and value[DOWNLEFT] == block and value[DOWNRIGHT] == block and value[LEFT] == blank and value[RIGHT] == blank and value[UPLEFT] == blank and value[UPRIGHT] == blank and value[UP] != block and dir == 2):
            client.walk_up()
        elif (value[RIGHT] == block and value[UPRIGHT] == block and value[DOWNRIGHT] == block and value[UP] == blank and value[DOWN] == blank and value[DOWNLEFT] == blank and value[UPLEFT] == blank and value[LEFT] != block and dir == 1):
            client.walk_left()
        elif (value[RIGHT] == block and value[UPRIGHT] == block and value[DOWNRIGHT] == block and value[UP] == blank and value[DOWN] == blank and value[DOWNLEFT] == blank and value[UPLEFT] == blank and value[LEFT] != block and dir == 2):
            client.walk_left()
        elif (value[DOWNLEFT] == block and value[DOWN] == blank and value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and dir == 1):
            client.walk_down()
        elif (value[DOWNLEFT] == block and value[DOWN] == blank and value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and dir == 2):
            client.walk_down()
        elif (value[DOWNLEFT] == block and value[DOWN] == blank and value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and dir == 3):
            client.walk_down()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == blank and value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and dir == 1):
            client.walk_right()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == blank and value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and dir == 2):
            client.walk_right()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == blank and value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and dir == 3):
            client.walk_right()
        elif (value[UPRIGHT] == block and value[UP] == blank and value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and dir == 1):
            client.walk_up()
        elif (value[UPRIGHT] == block and value[UP] == blank and value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and dir == 2):
            client.walk_up()
        elif (value[UPRIGHT] == block and value[UP] == blank and value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and dir == 3):
            client.walk_up()
        elif (value[UPLEFT] == block and value[LEFT] == blank and value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and dir == 1):
            client.walk_left()
        elif (value[UPLEFT] == block and value[LEFT] == blank and value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and dir == 2):
            client.walk_left()
        elif (value[UPLEFT] == block and value[LEFT] == blank and value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and dir == 3):
            client.walk_left()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[RIGHT] == blank and dir == 1):
            client.walk_right()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[RIGHT] == blank and dir == 2):
            client.walk_right()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[RIGHT] == blank and dir == 3):
            client.walk_right()
        elif (value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and value[RIGHT] == block and value[DOWNRIGHT] == block and value[UP] == blank and dir == 1):
            client.walk_up()
        elif (value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and value[RIGHT] == block and value[DOWNRIGHT] == block and value[UP] == blank and dir == 2):
            client.walk_up()
        elif (value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and value[RIGHT] == block and value[DOWNRIGHT] == block and value[UP] == blank and dir == 3):
            client.walk_up()
        elif (value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[UP] == block and value[UPRIGHT] == block and value[LEFT] == blank and dir == 1):
            client.walk_left()
        elif (value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[UP] == block and value[UPRIGHT] == block and value[LEFT] == blank and dir == 2):
            client.walk_left()
        elif (value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[UP] == block and value[UPRIGHT] == block and value[LEFT] == blank and dir == 3):
            client.walk_left()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and value[LEFT] == block and value[UPLEFT] == block and value[DOWN] == blank and dir == 1):
            client.walk_down()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and value[LEFT] == block and value[UPLEFT] == block and value[DOWN] == blank and dir == 2):
            client.walk_down()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and value[LEFT] == block and value[UPLEFT] == block and value[DOWN] == blank and dir == 3):
            client.walk_down()
        elif (value[UP] == block and value[UPLEFT] == block and value[UPRIGHT] == block and value[LEFT] != block):
            client.walk_left()
        elif (value[UPLEFT] == block and value[LEFT] == block and value[DOWNLEFT] == block and value[DOWN] != block):
            client.walk_down()
        elif (value[DOWNRIGHT] == block and value[DOWN] == block and value[DOWNLEFT] == block and value[RIGHT] != block):
            client.walk_right()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == block and value[UPRIGHT] == block and value[UP] != block):
            client.walk_up()
        elif (value[UP] == block and value[DOWN] == block and value[RIGHT] == block):
            client.walk_left()
        elif (value[UP] == block and value[DOWN] == block and value[LEFT] == block):
            client.walk_right()
        elif (value[RIGHT] == block and value[LEFT] == block and value[UP] == block):
            client.walk_down()
        elif (value[RIGHT] == block and value[LEFT] == block and value[DOWN] == block):
            client.walk_up()
        elif (dir == 1 and value[UP] == block and value[DOWN] == block):
            client.walk_right()
        elif (dir == 2 and value[UP] == block and value[DOWN] == block):
            client.walk_right()
        elif (dir == 3 and value[UP] == block and value[DOWN] == block):
            client.walk_right()
        elif (dir == 4 and value[UP] == block and value[DOWN] == block):
            client.walk_right()
        elif (value[UP] == block and value[DOWN] == block):
            client.walk_left()
        elif (dir == 1 and value[RIGHT] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 2 and value[RIGHT] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 3 and value[RIGHT] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 4 and value[RIGHT] == block and value[LEFT] == block):
            client.walk_up()
        elif (value[LEFT] == block and value[RIGHT] == block):
            client.walk_down()
        elif (dir == 1 and value[RIGHT] == block and value[UP] == block):
            client.walk_left()
        elif (dir == 2 and value[RIGHT] == block and value[UP] == block):
            client.walk_left()
        elif (dir == 3 and value[RIGHT] == block and value[UP] == block):
            client.walk_left()
        elif (dir == 4 and value[RIGHT] == block and value[UP] == block):
            client.walk_left()
        elif (value[RIGHT] == block and value[UP] == block):
            client.walk_down()
        elif (dir == 1 and value[UP] == block and value[LEFT] == block):
            client.walk_down()
        elif (dir == 2 and value[UP] == block and value[LEFT] == block):
            client.walk_down()
        elif (dir == 3 and value[UP] == block and value[LEFT] == block):
            client.walk_down()
        elif (dir == 4 and value[UP] == block and value[LEFT] == block):
            client.walk_down()
        elif (value[LEFT] == block and value[UP] == block):
            client.walk_right()
        elif (dir == 1 and value[DOWN] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 2 and value[DOWN] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 3 and value[DOWN] == block and value[LEFT] == block):
            client.walk_up()
        elif (dir == 4 and value[DOWN] == block and value[LEFT] == block):
            client.walk_up()
        elif (value[LEFT] == block and value[DOWN] == block):
            client.walk_right()
        elif (dir == 1 and value[DOWN] == block and value[RIGHT] == block):
            client.walk_up()
        elif (dir == 2 and value[DOWN] == block and value[RIGHT] == block):
            client.walk_up()
        elif (dir == 3 and value[DOWN] == block and value[RIGHT] == block):
            client.walk_up()
        elif (dir == 4 and value[DOWN] == block and value[RIGHT] == block):
            client.walk_up()
        elif (value[RIGHT] == block and value[DOWN] == block):
            client.walk_left()
        elif (value[UPRIGHT] == block and value[UPLEFT] == block and value[UP] == blank and dir == 1):
            client.walk_up()
        elif (value[UPRIGHT] == block and value[UPLEFT] == block and value[UP] == blank and dir == 2):
            client.walk_up()
        elif (value[UPRIGHT] == block and value[DOWNRIGHT] == block and value[RIGHT] == blank and dir == 1):
            client.walk_right()
        elif (value[UPRIGHT] == block and value[DOWNRIGHT] == block and value[RIGHT] == blank and dir == 2):
            client.walk_right()
        elif (value[DOWNLEFT] == block and value[UPLEFT] == block and value[LEFT] == blank and dir == 1):
            client.walk_left()
        elif (value[DOWNLEFT] == block and value[UPLEFT] == block and value[LEFT] == blank and dir == 2):
            client.walk_left()
        elif (value[DOWNLEFT] == block and value[DOWNRIGHT] == block and value[DOWN] == blank and dir == 1):
            client.walk_down()
        elif (value[DOWNLEFT] == block and value[DOWNRIGHT] == block and value[DOWN] == blank and dir == 2):
            client.walk_down()
        elif (value[UPLEFT] == block and value[UP] == blank and dir == 1):
            client.walk_up()
        elif (value[UPLEFT] == block and value[LEFT] == blank and dir == 2):
            client.walk_left()
        elif (value[UPRIGHT] == block and value[UP] == blank and dir == 3):
            client.walk_up()
        elif (value[UPRIGHT] == block and value[RIGHT] == blank and dir == 4):
            client.walk_right()
        elif (value[DOWNLEFT] == block and value[DOWN] == blank and dir == UP):
            client.walk_down()
        elif (value[DOWNLEFT] == block and value[LEFT] == blank and dir == LEFT):
            client.walk_left()
        elif (value[DOWNRIGHT] == block and value[DOWN] == blank and dir == RIGHT):
            client.walk_down()
        elif (value[DOWNRIGHT] == block and value[RIGHT] == blank and dir == DOWN):
            client.walk_right()
        elif (value[UP] == block and dir == UP):
            client.walk_down()
        elif (value[UP] == block and dir == RIGHT):
            client.walk_left()
        elif (value[UP] == block and dir == LEFT):
            client.walk_right()
        elif (value[LEFT] == block and dir == UP):
            client.walk_right()
        elif (value[LEFT] == block and dir == RIGHT):
            client.walk_up()
        elif (value[LEFT] == block and dir == LEFT):
            client.walk_down()
        elif (value[RIGHT] == block and dir == UP):
            client.walk_left()
        elif (value[RIGHT] == block and dir == RIGHT):
            client.walk_up()
        elif (value[RIGHT] == block and dir == LEFT):
            client.walk_down()
        elif (value[DOWN] == block and dir == UP):
            client.walk_up()
        elif (value[DOWN] == block and dir == RIGHT):
            client.walk_right()
        elif (value[DOWN] == block and dir == LEFT):
            client.walk_left()
        elif (value[UP] == block and dir == 1):
            client.walk_down()
        elif (value[UP] == block and dir == 2):
            client.walk_left()
        elif (value[UP] == block and dir == 3):
            client.walk_right()
        elif (value[UP] == block and dir == 4):
            client.walk_down()
        elif (value[UP] == block and dir == 5):
            client.walk_left()
        elif (value[UP] == block and dir == 6):
            client.walk_right()
        elif (value[LEFT] == block and dir == 1):
            client.walk_right()
        elif (value[LEFT] == block and dir == 2):
            client.walk_up()
        elif (value[LEFT] == block and dir == 3):
            client.walk_down()
        elif (value[LEFT] == block and dir == 4):
            client.walk_right()
        elif (value[LEFT] == block and dir == 5):
            client.walk_up()
        elif (value[LEFT] == block and dir == 6):
            client.walk_down()
        elif (value[RIGHT] == block and dir == 1):
            client.walk_left()
        elif (value[RIGHT] == block and dir == 2):
            client.walk_up()
        elif (value[RIGHT] == block and dir == 3):
            client.walk_down()
        elif (value[RIGHT] == block and dir == 4):
            client.walk_left()
        elif (value[RIGHT] == block and dir == 5):
            client.walk_up()
        elif (value[RIGHT] == block and dir == 6):
            client.walk_down()
        elif (value[DOWN] == block and dir == 1):
            client.walk_up()
        elif (value[DOWN] == block and dir == 2):
            client.walk_right()
        elif (value[DOWN] == block and dir == 3):
            client.walk_left()
        elif (value[DOWN] == block and dir == 4):
            client.walk_up()
        elif (value[DOWN] == block and dir == 5):
            client.walk_right()
        elif (value[DOWN] == block and dir == 6):
            client.walk_left()
        elif value[UP] == block:
            client.walk_down()
        elif value[LEFT] == block:
            client.walk_right()
        elif value[RIGHT] == block:
            client.walk_left()
        elif value[DOWN] == block:
            client.walk_up()
        

        elif dir == UP:
            client.walk_up()
        elif dir  == LEFT:
            client.walk_left()
        elif dir == RIGHT:
            client.walk_right()
        elif dir == DOWN:
            client.walk_down()
        elif dir == 1:
            client.walk_up()
        elif dir == 2:
            client.walk_left()
        elif dir == 3:
            client.walk_right()
        elif dir == 4:
            client.walk_down()
        elif dir == 5:
            client.walk_up()
        elif dir == 6:
            client.walk_left()
        elif dir == 7:
            client.walk_right()
        elif dir == 8:
            client.walk_down()
        else:
            client.look_down()


if __name__ == "__main__":
    main()