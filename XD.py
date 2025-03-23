# Import các thư viện cần thiết
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# 1. Đọc dữ liệu từ file Excel
file_path = "data3.xlsx"  # Đường dẫn file đã tải lên

try:
    df = pd.read_excel(file_path, sheet_name="Sheet1")
except FileNotFoundError:
    raise FileNotFoundError("Không tìm thấy file data3.xlsx. Hãy kiểm tra lại đường dẫn.")

# 2. Chuẩn hóa tên cột để tránh lỗi
df.columns = df.columns.str.strip().str.replace(":", "", regex=True)
print("Tên cột sau khi chuẩn hóa:", df.columns.tolist())  # Kiểm tra danh sách cột

# 3. Xác định các cột đặc trưng và biến mục tiêu
feature_columns = [
    "Giới tính của Anh/Chị là",
    "Tình trạng hiện tại",
    "Bạn có sử dụng thiết bị điện tử trước khi ngủ",
    "Thời gian ngủ trong một đêm",
    "Bạn có tỉnh giấc giữa đêm không",
    "Mức độ căng thẳng trong ngày"
]
target_column = "Chất lượng giấc ngủ hiện tại"

# 4. Kiểm tra sự tồn tại của các cột
missing_columns = [col for col in feature_columns + [target_column] if col not in df.columns]
if missing_columns:
    raise ValueError(f"Cột không tồn tại trong dữ liệu: {missing_columns}")

# 5. Loại bỏ các dòng thiếu giá trị ở cột mục tiêu
df = df.dropna(subset=[target_column])

# 6. Chuyển dữ liệu dạng chuỗi thành dạng số bằng LabelEncoder
label_encoders = {}
for col in feature_columns + [target_column]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))  # Chuyển đổi dữ liệu
    label_encoders[col] = le  # Lưu lại encoder để giải mã nếu cần

# 7. Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X = df[feature_columns]
y = df[target_column]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)

# 8. Huấn luyện mô hình cây quyết định với Entropy
clf = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
clf.fit(X_train, y_train)

# 9. Dự đoán và đánh giá mô hình
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"🎯 Độ chính xác của mô hình: {accuracy:.2f}")

# 10. Vẽ Confusion Matrix
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues',
            xticklabels=label_encoders[target_column].classes_,
            yticklabels=label_encoders[target_column].classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix - Đánh giá mô hình cây quyết định")
plt.show()

# 11. Vẽ cây quyết định
plt.figure(figsize=(15, 10))
plot_tree(clf, filled=True, feature_names=feature_columns, class_names=label_encoders[target_column].classes_, fontsize=4)
plt.title("Cây quyết định về Chất lượng giấc ngủ", fontsize=16)  # Tăng kích thước tiêu đề
plt.show()

