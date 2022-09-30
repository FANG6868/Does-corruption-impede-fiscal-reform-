from snownlp import SnowNLP

text1 = ''
text2 = ''

s1 = SnowNLP(text1)
s2 = SnowNLP(text2)

print(s1.sentiments,s2.sentiments)

def snow_result(comemnt):
    s = SnowNLP(comemnt)
    if s.sentiments >= 0.6:
        return 1
    else:
        return 0

data['snlp_result'] = data.comment.apply(snow_result)

data.head(5)

counts = 0
for i in range(len(data)):
    if data.iloc[i,2] == data.iloc[i,3]:
        counts+=1

print(counts/len(data))