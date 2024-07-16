#SECTION -------------------------------------------------------------------------------------------------------------------
#*******************************************************
# if __name__ = '__main__
#*******************************************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

#   Python interpreter sets "special variables", one of which is__name__ 
#   then Python will execute the code found within _main_
# import module_2
# print(__name__)
# print(module_2.__name__)

# if __name__=='__main__':
#     print('running this module directly')
# else:
#     print('running other modules indirectly')


# def hello():
#     print("Hello")

# if(__name__=='__main__'):
#     hello()


def documentFunc(x):
    print(f"We want to print {x}")