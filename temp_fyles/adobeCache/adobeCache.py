import os


def adobe_cache(username):
    #Verifies if the actual version of reader is DC or 10.0
    if os.path.exists(f'C:\\Users\\{username}\\AppData\\Local\\Adobe\\Acrobat\\DC\\Cache') == True:
        os.chdir(f'C:\\Users\\{username}\\AppData\\Local\\Adobe\\Acrobat\\DC\\Cache')
        for filename in os.listdir():
            os.remove(filename)

    elif os.path.exists(f'C:\\Users\\{username}\\AppData\\Local\\Adobe\\Acrobat\\10.0\\Cache') == True:
        os.chdir(f'C:\\Users\\{username}\\AppData\\Local\\Adobe\\Acrobat\\10.0\\Cache')
        for filename in os.listdir():
            os.remove(filename)
