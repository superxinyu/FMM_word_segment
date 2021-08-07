from FMM import tokenize_fmm,load_dict

sentence="武汉市长江大桥发表重要讲话"
word_set,max_len_word=load_dict("./word_set.txt")
print(tokenize_fmm(sentence=sentence,word_set=word_set,max_len_word=max_len_word))