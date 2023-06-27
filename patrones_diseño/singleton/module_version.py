from test_singleton import singletonTest, singleton_test



def main():
    
    singleton_1 = singleton_test
    singleton_2 = singleton_test
    
    print(singleton_1 is singleton_2)

if __name__ == "__main__":
    main()
    
