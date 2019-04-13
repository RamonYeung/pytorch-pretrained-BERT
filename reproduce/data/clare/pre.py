data_train = []
data_test = []
id2label = []
label2id = {}

with open('./train_data.csv', encoding='utf-8') as f:
    f.readline()
    for line in f:
        intent, text = line.split(',', 1)
        text = text.strip()

        if intent not in id2label:
            id2label.append(intent)
            label2id[intent] = len(id2label) - 1
        
        data_train.append("{}\t\t\t{}\t\t".format(label2id[intent],
                                                  text.lower()))


with open('./test_data.csv', encoding='utf-8') as f:
    f.readline()
    for line in f:
        intent, text = line.split(',', 1)
        text = text.strip()

        if intent not in id2label:
            id2label.append(intent)
            label2id[intent] = len(id2label) - 1
        
        data_test.append("{}\t\t\t{}\t\t".format(label2id[intent],
                                                  text.lower()))

with open('./train.tsv', 'w', encoding='utf-8') as g:
    for i in data_train:
        g.write(i + '\n')

with open('./dev.tsv', 'w', encoding='utf-8') as g:
    for i in data_test:
        g.write(i + '\n')

