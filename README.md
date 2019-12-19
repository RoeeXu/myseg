myseg
=====

your_dict.txt:

    吃 1 symptom
    什么 1 stop
    药物 1 unlabeled
    可以 1 stop
    流产 1 disease-symptom-operation-gender

INPUT:

    import myseg
    dt = myseg.Tokenizer('your_dict.txt')
    print(list(dt.cut('吃什么药物可以流产', HMM=False)))

OUTPUT:

    [pair('吃', 'symptom'), pair('什么', 'stop'), pair('药物', 'unlabeled'), pair('可以', 'stop'), pair('流产', 'disease-symptom-operation-gender')]
