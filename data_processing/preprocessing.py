"""
This script is intended to hold all the functions used to prepare the data 
after EDA. Take all the transformations, new features, etc, and place the
functions used to perform those transformations or create those features here.

NOTE: It is important to call all processing functions inside the predefined 
function present in this file because it will be called during the training 
pipeline.
"""

def test1():
    return "this is a test"

def test2(input: str):
    return input + ", " + "this is a test 2"

def test3(input: str):
    return input + ", " + "this is a test 3"

def main():
    """
    This is the main driver for this script and will be called in the training
    pipeline. Put all the required preprocessing function calls here.
    """

    processed = test1()
    processed = test2(processed)
    processed = test3(processed)
    
    return processed

if __name__ == "__main__":
    print(main())