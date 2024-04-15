import pandas as pd
import folium

# 讀取CSV文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638488057641011625.csv', encoding='big5', skiprows=1)

# 提取地震位置的經緯度
locations = df[['C', 'D']].values

# 創建一個新的folium地圖實例
m = folium.Map(location=[locations[0][0], locations[0][1]], zoom_start=13)

# 使用從DataFrame中提取的經緯度數據創建Polygon並添加到地圖上
for location in locations:
    folium.Polygon([location], color="red", fill=True, fill_color="red").add_to(m)

# 保存地圖到指定的工作區
m.save('/workspaces/cycu_ai2024/20240409/earthquake_map.html')