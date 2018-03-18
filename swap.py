def main():
    x = input('Input two numbers: ')
    a, b = map(int, x.split())
    if a < b:
        a, b = b, a
        
    print(a,b)
    
main()
