import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# ========== 1. 建立假資料 ==========
# 模擬貸款審核資料
torch.manual_seed(42)
X = torch.randn(200, 4)  # 200 筆，4 個特徵，[月收入, 信用評分, 負債比率, 工作年資]
y = (X[:, 0] + X[:, 1] > 0).float().unsqueeze(1)  # 標籤，1 = 核准，0 = 拒絕


# ========== 2. 建立 DataLoader ==========
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)


# ========== 3. 定義模型 ==========
class BinaryClassifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 8), nn.ReLU(), nn.Linear(8, 1), nn.Sigmoid()
        )

    def forward(self, x):
        return self.net(x)


model = BinaryClassifier()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)


# ========== 4. 訓練迴圈 ==========
EPOCHS = 20

for epoch in range(EPOCHS):
    total_loss = 0
    for X_batch, y_batch in loader:
        # 前向傳播
        y_pred = model(X_batch)
        loss = criterion(y_pred, y_batch)

        # 反向傳播
        optimizer.zero_grad()  # 清除舊梯度
        loss.backward()  # 計算梯度
        optimizer.step()  # 更新權重

        total_loss += loss.item()

    avg_loss = total_loss / len(loader)
    print(f"Epoch [{epoch + 1:02d}/{EPOCHS}] | Loss: {avg_loss:.4f}")


# ========== 5. 推論 ==========
# 推論結果解讀
model.eval()

with torch.no_grad():
    sample = torch.randn(1, 4)  # 一位新客戶的資料
    output = model(sample)
    prob = output.item()
    result = "✅ 核准貸款" if prob > 0.5 else "❌ 拒絕貸款"
    print(f"核准機率: {prob:.4f}")
    print(f"審核結果: {result}")
