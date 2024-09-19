import torch
import torch.nn as nn

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNetwork, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)

        self.selu = nn.SELU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.selu(out)
        out = self.l2(out)
        out = self.selu(out)
        out = self.l3(out)
        
        return out
    
# class NeuralNetwork2(nn.Module):
#     def __init__(self, input_size, hidden_size, num_classes):
#         super(NeuralNetwork2, self).__init__()
#         self.l1 = nn.Linear(input_size, hidden_size)
#         self.l2 = nn.Linear(hidden_size, num_classes)

#         self.relu = nn.ReLU()
#         self.dropout = nn.Dropout(p=0.5)  # Adding dropout for regularization
    
#     def forward(self, x):
#         out = self.l1(x)
#         out = self.relu(out)
#         out = self.dropout(out)  # Apply dropout after ReLU
#         out = self.l2(out)

#         # no activation and no softmax at the end
#         return out