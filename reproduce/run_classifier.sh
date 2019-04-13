export GLUE_DIR=./data/
export TASK_NAME=clare

python run_classifier.py \
  --task_name $TASK_NAME \
  --do_train \
  --do_eval \
  --do_lower_case \
  --data_dir $GLUE_DIR/$TASK_NAME \
  --bert_model ./pretrains/uncased/ \
  --max_seq_length 32 \
  --train_batch_size 32 \
  --learning_rate 2e-5 \
  --num_train_epochs 80.0 \
  --output_dir /tmp/$TASK_NAME/
