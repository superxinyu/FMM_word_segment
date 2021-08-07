def load_dict(file_path):
    f = open(file_path, "r", encoding="utf-8")
    word_set = set()
    max_len_word = 0
    for line in f:
        word = line.strip()
        word_set.add(word)
        if len(word) > max_len_word:
            max_len_word = len(word)
    f.close()

    return word_set, max_len_word


def tokenize_fmm(sentence, word_set, max_len_word):
    """
    用FMM算法切词，步骤就是设置左右边界，不断缩小右边界，直到边界内的单词在词库里
    :param sentence: 带切分句子
    :param word_set: 词库
    :param max_len_word: 词典中最长的单词
    :return: 切割单词列表
    """
    begin = 0
    end = min(begin + max_len_word, len(sentence))
    word_seg_list = []
    while begin < end:
        word = sentence[begin:end]
        if word in word_set or end - begin == 1:
            word_seg_list.append(word)
            begin = end
            end = min(begin + max_len_word, len(sentence))
        else:
            end -= 1
    return word_seg_list
