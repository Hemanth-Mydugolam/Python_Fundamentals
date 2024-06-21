import argparse

def main_func():
    """
    This function accepts name and age of an employee
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='Specify a name')
    parser.add_argument('--age', type=int, help='Specify an age')
    
    args = parser.parse_args()
    name = args.name
    age = args.age
    
    if name and age:
        print(f"Hello {name}! You are {age} years old.")
    else:
        raise Exception("Both name and age are not provided.")
        
if __name__ == "__main__":
    main_func()