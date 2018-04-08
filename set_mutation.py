int(raw_input())
n=set(raw_input().split())
#x=int(raw_input())
for i in range(input()):
    m=raw_input().split()
    getattr(n,m[0])(set(raw_input().split()))
    
            
print sum(map(int,n))
        
