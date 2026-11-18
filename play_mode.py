from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie
import random

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            game_world.toggle_bb()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy, 1)

    grass = Grass()
    game_world.add_oject(grass, 0)

    balls = [Ball(random.randint(100, 1600 - 100), 60, 0) for _ in range(30)]
    game_world.add_objects(balls, 1)



def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()
    for o in game_world.world[1][:]:  # 던진 공까지 월드의 모든 공이 대상 (제거해도 되도록 복사본으로 순회)
        if isinstance(o, Ball) and game_world.collide(boy, o):
            print('COLLISION boy : ball')
            game_world.remove_object(o)
def render():
    clear_canvas()
    game_world.render()
    update_canvas()









