# Setup environment

Run command below in CMD
1. Create new enviromnent
2. Activate the enviroment
3. Install all package mentions in requirements.txt

```cmd
python -m venv env
env\Scripts\activate.bat  
pip install -r requirements.txt
```

# Using Nvidia GPU for training (Optional)
```cmd
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

# Create requirements.txt (For contributor only)
```cmd
pip freeze > requirements.txt
```

# Activate environment

```cmd
env\Scripts\activate.bat  
```

# How to deactivate environment

Run command below in CMD

```cmd
deactivate
```


# Resource
[Dataset for chatbot](https://www.kaggle.com/datasets/grafstor/simple-dialogs-for-chatbot?resource=download) <br>
[Computer hardware dataset](https://www.kaggle.com/datasets/dilshaansandhu/general-computer-hardware-dataset/data) <br>
[Dataset](https://github.com/Thavarshan/nesbot/blob/main/intents.json#L2)