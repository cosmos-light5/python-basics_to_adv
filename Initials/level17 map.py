numbers=[1,2,3,4,5,6,7,8,9,10]
greater_than_five=list(filter(lambda x:x>5, numbers))
print(greater_than_five)

words=['hi','hello','bye','good_bye','yes','no']
more_than_three=list(filter(lambda word:len(word)>3, words))
print(more_than_three)

word_with_h=list(filter(lambda word:"h" in word, words))
print(word_with_h)