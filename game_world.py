from pico2d import draw_rectangle

world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

show_bb = True  # B 키로 충돌 박스 표시를 켜고 끈다

def toggle_bb():
    global show_bb
    show_bb = not show_bb

def draw_bb(o):
    if show_bb:
        draw_rectangle(*o.get_bb())

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()




def clear():
    for layer in world:
        layer.clear()
