
import os

def walk(dirname):
    """Prints the names of all files in dirname and its subdirectories.

    dirname: string name of directory
    """
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print path
        else:
            walk(path)



if __name__ == '__main__':
    walk('.')

    
