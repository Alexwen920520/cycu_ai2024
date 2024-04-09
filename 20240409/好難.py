import pandas as pd
import folium

# 讀取CSV數據
data = pd.read_csv("地震活動彙整_638482892289528484.csv")

# 創建一個新的地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 創建一個用於存儲地點的列表
locations = []

# 對每一個地震，獲取其地點，並添加到地圖上
for index, row in data.iterrows():
    # 從數據中獲取地點
    location = [row['latitude'], row['longitude']]
    # 將地點添加到列表中
    locations.append(location)

# 使用PolyLine繪製地震震央的連接線
folium.PolyLine(locations).add_to(m)

# 使用Polygon繪製地震震央的多邊形
folium.Polygon(locations).add_to(m)

# 將地圖保存為一個HTML文件
m.save("earthquake_map.html")