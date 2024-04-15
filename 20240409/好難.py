import pandas as pd
import folium

# 讀取CSV文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638488057641011625.csv', encoding='big5', skiprows=1)

# 提取地震位置的經緯度
locations = df[['緯度', '經度']].values
magnitudes = df['規模'].values
depths = df['深度'].values
places = df['位置'].values
times = df['地震時間'].values

# 創建一個新的folium地圖實例
m = folium.Map(location=[locations[0][0], locations[0][1]], zoom_start=13)

# 使用從DataFrame中提取的經緯度數據創建Marker並添加到地圖上
for i, location in enumerate(locations):
    tooltip_text = f"地震時間：{times[i]}<br>" \
                   f"位置：北緯 {location[0]}度，東經 {location[1]}度<br>" \
                   f"即在{places[i]}<br>" \
                   f"地震深度：{depths[i]}公里<br>" \
                   f"芮氏規模：{magnitudes[i]}"
    folium.Marker(location, tooltip=tooltip_text, color="red", fill=True, fill_color="red").add_to(m)

# 保存地圖到指定的工作區
m.save('/workspaces/cycu_ai2024/20240409/earthquake_map.html')