import sys
input = sys.stdin.readline

N = int(input().strip())

dic = {'Algorithm':204
       ,'DataAnalysis':207
       ,'ArtificialIntelligence':302
       ,'CyberSecurity':'B101'
       ,'Network':303
       ,'Startup':501
       ,'TestStrategy':105
       }

for i in range(N):
    print(dic.get(input().strip()))
