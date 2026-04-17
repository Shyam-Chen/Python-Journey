import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np


# 1. 生成模擬數據
# 真實關係: y = 3x + 2 + noise
torch.manual_seed(42)
X = torch.randn(100, 1) * 10  # 100 個樣本，1 個特徵
y = 3 * X + 2 + torch.randn(100, 1) * 2  # 加入噪音


# 2. 定義線性回歸模型
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super(LinearRegressionModel, self).__init__()
        self.linear = nn.Linear(1, 1)  # 輸入維度 1，輸出維度 1

    def forward(self, x):
        return self.linear(x)


# 3. 初始化模型、損失函數和優化器
model = LinearRegressionModel()
criterion = nn.MSELoss()  # 均方誤差損失
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 隨機梯度下降


# 4. 訓練模型
epochs = 100
losses = []

for epoch in range(epochs):
    # 前向傳播
    y_pred = model(X)

    # 計算損失
    loss = criterion(y_pred, y)
    losses.append(loss.item())

    # 反向傳播
    optimizer.zero_grad()  # 清空梯度
    loss.backward()  # 計算梯度
    optimizer.step()  # 更新參數

    # 每 10 個 epoch 印出一次
    if (epoch + 1) % 10 == 0:
        print(f"Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}")


# 5. 查看學習到的參數
weight = model.linear.weight.item()
bias = model.linear.bias.item()
print(f"\n學習到的參數: y = {weight:.2f}x + {bias:.2f}")
print("真實參數: y = 3.00x + 2.00")


# 6. 視覺化結果
plt.figure(figsize=(12, 4))

# 中文字體
plt.rcParams["font.sans-serif"] = [
    "Microsoft JhengHei",
    "PingFang TC",
    "Noto Sans CJK TC",
]

# 負號顯示
plt.rcParams["axes.unicode_minus"] = False

# 左圖：數據和擬合線
plt.subplot(1, 2, 1)
plt.scatter(X.numpy(), y.numpy(), alpha=0.5, label="原始數據")
plt.plot(X.numpy(), y_pred.detach().numpy(), "r", label="擬合線", linewidth=2)
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("線性回歸擬合結果")

# 右圖：損失曲線
plt.subplot(1, 2, 2)
plt.plot(losses)
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("訓練損失曲線")
plt.grid(True)

plt.tight_layout()
plt.show()
