# OpenVino_Chatbot
# Q&A Chatbot for OpenVINO web documentation by OpenVINO

Running GenAI on Intel AI Laptops with Simple LLM Inference on CPU and Fine-Tuning of LLM Models using Intel OpenVINO. The program can answer your questions by referring the OpenVINO technical documentation from the OpenVINO official web site.

This program doesn't rely on any cloud services or webAPIs for inferencing. The program downloads all the data, including reference documents and DL models, and **can perform inference offline**. You don't need any cloud services once you prepare the data locally. 

## How To Run:
1. Create Virtual Environment:
```
python -m venv venv
venv/Scripts/activate
```
2. Install Requirements:
```
python -m pip install -U pip
pip install -U setuptools wheel
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
3.Download documentation:
We can download docs or we can also use beautifulSoup. Save the contents in "files_html_doc"
After downloading run this script:
```
python openvino-doc-specific-extractor.py
```
4. Download the models:
neural-chat-7b OR llama2-7b 
Access API on huggingface website
Run the Script:
```
python llm-model-downloader.py
```
5.Run the server:
```
uvicorn openvino-rag-server:app --host 0.0.0.0
```
6. Run the client:
```
streamlit run openvino-rag-client.py
```

## Programs / Files

|#|Program/File|Description|
|---|---|---|
|1|`llm-model-downloader.py`|Download intel/neural-chat-7b and meta-llama/llama2-7b-chat models, and convert them into OpenVINO IR models.|
|2|`openvino-doc-specific-extractor.py`|Convert OpenVINO HTML documents into vector store (DB)|
|3|`openvino-server.py`|OpenVINO Q&A server|
|4|`openvino-client.py`|OpenVION Q&A client|
|5|`.env`|Configurations file|
|6|`requirements.txt`|Python module requirements file|
|7|`huggingface_login.py`|Login to HuggingFace hub.|



