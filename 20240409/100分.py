import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson

# 讀取CSV文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240409/地震活動彙整_638488057641011625.csv', encoding='big5', skiprows=1)

# 提取地震位置的經緯度
locations = df[['緯度', '經度']].values
magnitudes = df['規模'].values
depths = df['深度'].values
places = df['位置'].values
times = pd.to_datetime(df['地震時間']).astype(int) / 10**9  # 轉換為Unix時間戳

# 創建一個新的folium地圖實例
m = folium.Map(location=[locations[0][0], locations[0][1]], zoom_start=13)

# 創建一個包含所有地震數據的GeoJson對象
features = [
    {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [lon, lat],
        },
        'properties': {
            'time': time * 1000,  # 轉換為JavaScript的時間戳
            'style': {'color' : 'red'},
            'icon': 'circle',
            'popup': f"<div style='font-size:12px;'>地震時間：{pd.to_datetime(time, unit='s')}<br>" \
                     f"位置：北緯 {lat}度，東經 {lon}度<br>" \
                     f"即在{place}<br>" \
                     f"地震深度：{depth}公里<br>" \
                     f"芮氏規模：{magnitude}</div>",
            'iconstyle': {
                'fillColor': 'red',
                'fillOpacity': 0.6,
                'stroke': 'false',
                'radius': 5
            }
        }
    }
    for lat, lon, time, place, depth, magnitude in zip(locations[:, 0], locations[:, 1], times, places, depths, magnitudes)
]

# 將GeoJson對象添加到地圖上
TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': features},
    period='PT1H',
    add_last_point=False,
).add_to(m)

# 保存地圖到指定的工作區
m.save('/workspaces/cycu_ai2024/20240409/earthquake_map.html')