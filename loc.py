import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# 📌 Đọc dữ liệu từ file Excel (Sheet1)
file_path = "data3.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

# 📌 Hiển thị danh sách cột để kiểm tra
print("Các cột trong dữ liệu:", df.columns)

# 📌 Xác định cột mục tiêu (cột chứa nhãn mà mô hình cần dự đoán)
target_column = "Chất lượng giấc ngủ hiện tại:"  # Đổi tên nếu cần

# 📌 Kiểm tra xem cột mục tiêu có tồn tại không
if target_column not in df.columns:
    raise ValueError(f"Cột mục tiêu '{target_column}' không tồn tại trong dữ liệu!")

# 📌 X (đặc trưng) và y (nhãn)
X = df.drop(columns=[target_column])
y = df[target_column]

# 📌 Xử lý dữ liệu: Mã hóa các biến phân loại thành số
X = pd.get_dummies(X)  # Chuyển đổi biến phân loại thành dạng số

# 📌 Chia tập dữ liệu thành train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 📌 Huấn luyện mô hình Decision Tree
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# 📌 Dự đoán và tính độ chính xác
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Độ chính xác mô hình: {accuracy:.4f}")

# 📌 Xuất 30 dòng dữ liệu gốc để test vẽ cây trong Excel
df_selected = df.iloc[:30]  # Chọn 30 dòng đầu tiên
output_path = "G:/CIT/data_test_original.xlsx"
df_selected.to_excel(output_path, index=False)

print(f"✅ Đã lưu 30 dòng dữ liệu vào file: {output_path}")

# 📌 Xuất cây quyết định dưới dạng văn bản
tree_rules = export_text(model, feature_names=list(X.columns))
print("\n📌 Cây quyết định được tạo:")
print(tree_rules)
