import misc_tools
import random

INIT_QT = 1000

def create_routing(env, first_step='move1'):

    tasks={
        'move1': {
            'location': env['forklift'], #was env['multiplexer_storage']
            'worker': env['production_control'],
            'manned': True,
            'setup_time': 0,
            'run_time': 0,
            'teardown_time': 0,
            'transit_time': 0.1,
            'route_to': env['antenna_kit_kanban']
        }
    }


    return misc_tools.make_steps(first_step=first_step, tasks=tasks)

def create_kanban_attrs(env):

    return misc_tools.make_kanban_attrs(order_gen=env['gener.antenna_kit'],
        order_point=20, order_qty=50,
        init_qty=INIT_QT, warmup_time=0)
    # what are the details of this specific kanban?order point, order quantity, etc.
    # because I just made mine up

#init qty: 50

	
