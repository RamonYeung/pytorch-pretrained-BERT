### Reproduction Notes

This README serves as a quick note on how to fine-tune the BERT. It has some pointers to things that I spent a lot time to figure out.

- download the `uncased` version of [small BERT](https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased.tar.gz), and the corresponding `vocab.txt` is provided in `./preatrains/uncased/`. Note that the filename of vocabulary is hard coded in the source code **so you should always manaully rename the downloaded file to `vocab.txt` under some folder along with the untar model files.**
- other version of pretrain models can be found [here](https://github.com/huggingface/pytorch-pretrained-BERT/blob/master/pytorch_pretrained_bert/modeling.py#L39-L47).
- other version of corresponding vocab.txt can be found [here](https://github.com/huggingface/pytorch-pretrained-BERT/blob/master/pytorch_pretrained_bert/tokenization.py#L29-L37).
- download your data file and put it in `data/$TASK_NAME` subfolder.
- filenames of train and test data have to be `train.tsv` and `dev.tsv` with '\t' as seperator, respectively. I have prepared a pre.py in `data/clare` subfolder.
- the external dependency is PyTorch 0.4+.

Go throught the above bullet points and run the code by typing: `sh run_classifier.sh` 

