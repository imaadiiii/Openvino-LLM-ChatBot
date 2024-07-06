#llm-model-downloader.py
import shutil
import logging
import os
import gc
from pathlib import Path
from dotenv import load_dotenv

from huggingface_hub import login, whoami
from optimum.intel import OVQuantizer
from optimum.intel.openvino import OVModelForCausalLM
import openvino as ov
import nncf

nncf.set_log_level(logging.ERROR)

load_dotenv(verbose=True)
cache_dir = os.environ['CACHE_DIR']

def prepare_model(model_vendor, model_id, group_size:int, ratio:float, int4_mode:str='SYM', generate_fp16:bool=True, cache_dir='./cache'):
    pt_model_id = f'{model_vendor}/{model_id}'
    fp16_model_dir = Path(model_id) / "FP16"

    ov_model_file_name = 'openvino_model.xml'

    print(f'** Prepaing model : {model_vendor}/{model_id}')

    # FP16
    if generate_fp16 and not os.path.exists(fp16_model_dir / ov_model_file_name):
        print('\n** Generating an FP16 IR model')
        ov_model = OVModelForCausalLM.from_pretrained(pt_model_id, export=True, compile=False, cache_dir=cache_dir, ov_config={'CACHE_DIR':cache_dir})
        ov_model.half()
        ov_model.save_pretrained(fp16_model_dir)
        del ov_model
        gc.collect()
    else:
        print('\n** Skip generation of FP16 IR model (directory already exists)')



print('*** LLM model downloader')

# Intel/neural-chat-7b
prepare_model('Intel', 'neural-chat-7b-v3-1', group_size=64, ratio=0.6)


# meta/Llama2-7b-chat
try:
    whoami()
    print('Authorization token already provided')
except OSError:
    print('The llama2 model is a controlled model.')
    print('You need to login to HuggingFace hub to download the model.')
    login()
finally:
    prepare_model('meta-llama', 'Llama-2-7b-chat-hf', group_size=128, ratio=0.8)

