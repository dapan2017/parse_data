
import pandas as pd
import json
from predictobstacle import PredictObstacle

data_path = "/Users/panjiqing/Desktop/licode/data/predict_data/_viz_prediction_pred_obstacles.csv"

# data = pd.read_csv(data_path ,  error_bad_lines=False)
# print(data)

with open(data_path, 'r',encoding='utf-8-sig') as f:
    # 循环每行
    for line in f:
        # 将每行处理后为列表，再添加到data中
        if line != '_viz_prediction_pred_obstacles\n':
            # print(json.loads(line)["markers"])
            data = json.loads(line)["markers"]
            if len(data) > 0:
                for obs in data:
                    print(PredictObstacle(obs).label)
            # print(line)

            

#         data.append(list(line.strip().split(',')))


