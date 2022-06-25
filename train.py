import yaml
import subprocess

config = yaml.safe_load(open('config/params.yaml'))
train_path          = config['path']['train']
val_path            = config['path']['val']
pretrain_path       = config['path']['pretrain']
model_load_path     = config['path']['model_load']
model_write_path    = config['path']['model_write']
model_type          = config['train']['model_type']
per_gpu_batch_size  = config['train']['per_gpu_batch_size']
gradient_steps      = config['train']['gradient_steps']
num_train_epochs    = config['train']['num_train_epochs']
block_size          = config['train']['block_size']

subprocess.run("git clone https://github.com/sberbank-ai/ru-gpts")

command = f"""python {pretrain_path} \
    --output_dir={model_write_path} \
    --model_type={model_type} \
    --model_name_or_path={model_load_path}  \
    --do_train \
    --train_data_file={train_path} \
    --do_eval \
    --eval_data_file={val_path} \
    --per_gpu_train_batch_size {per_gpu_batch_size} \
    --gradient_accumulation_steps {gradient_steps} \
    --num_train_epochs {num_train_epochs} \
    --block_size {block_size} \
    --overwrite_output_dir"""

list_files = subprocess.run(command)
print("The exit code was: %d" % list_files.returncode)