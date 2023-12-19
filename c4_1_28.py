def say_something(word, *args):
    print('word=', word)
    for arg in args:
        print(arg)
        
say_something('朝', '昼', '夜')    