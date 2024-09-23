# Setup environment

Run command below in CMD
1. Create new enviromnent
2. Activate the enviroment
3. Install all package mentions in requirements.txt <br>

Need some time to install all of the package be patient

```cmd
python -m venv env
env\Scripts\activate.bat  
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
If failed to install the requirement. Run:
```
pip install numpy nltk torch torch-vision flask flask-cors textblob pandas scikit-learn
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

# Must train model first before running chatbot
Run ```python backend\train.py```

# How to enable API requests (MNN)
Run ```python backend\chat_api.py```

# To enable API Request KNN
Run ```python backend\chat_api_knn.py```

# To start UI
Right click the index.php and choose PHP Server: Serve Project

# To reload UI
Right click index.php and choose PHP Server: Reload Project

# To run iBanana for KNN
1. Run API request first to initiate port
2. Start UI/Reload UI

# To test accuracy for KNN
```python backend\accuracy_test_copy.py```

# To test accuracy for MNN
```python backend\accuracy_test.py```


# To run iBanana for MNN
1. Train 
2. Run API request first to initiate port
3. Start UI/Reload UI

# How to chat with bot locally (MNN - CLI interface)
Run ```python backend\chat_local.py```


# Resource
[Computer hardware dataset](https://www.kaggle.com/datasets/dilshaansandhu/general-computer-hardware-dataset/data) <br>
[Dataset](https://github.com/Thavarshan/nesbot/blob/main/intents.json#L2)
