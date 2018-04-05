if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    x=max(arr)
    while (x==max(arr)):
        arr.remove(x)
    print max(arr)
            
        
        
    
