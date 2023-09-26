import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self, input_size=6, hidden_size=20, output_size=1, layers=3):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, layers, batch_first=True, bidirectional=True)
        self.linear = nn.linear(hidden_size * 2, output_size)
        self.function = torch.sigmoid

    def forward(self, x):
        x, hidden = self.lstm(x, None)
        x = x[:, -1, :]
        x = self.linear(x)
        x = self.function(x)
        return x


net = Net()

import torch.optim as op

criteria = nn.MSELoss()
optimiser = op.Adam(net.parameters())
EPCHO = 10

