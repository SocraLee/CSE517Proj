# Extracting Prompts by Inverting LLM Outputs

## Requirements

To install requirements:

```setup
# download the dataset and models
wget "https://zenodo.org/records/12759549/files/prompt2output_inverters.zip?download=1" -O prompt2output_inverters.zip
wget "https://zenodo.org/records/12759549/files/prompt2output_datasets.zip?download=1" -O prompt2output_datasets.zip
unzip prompt2output_inverters.zip
unzip prompt2output_datasets.zip
pip install .
```

## Troubleshooting
If you encountered problems while running the code, please make sure your `transformers` library version is 4.36.0 and `accelarate` version is 0.28.0, if it is too new, there will be problem 

## Training

To train the model(s) in the paper, run this command:

```train
python main.py {train/test} {task section} {dataset} {number of outputs}
# example usage 
python main.py train user_prompts sharegpt 64
python main.py test system_prompts sharegpt 1

```

user prompts dataset that you can test with
```
chat_instruction2m
lm_instruction2m
sharegpt
unnatural
```

For your convenience, you can directly use train.sh/test.sh to train/evaluate all tasks (remember to specify where to load the ckpt in the script).
## Pre-trained Models

The pre-trained models are in the `inverters` folder
