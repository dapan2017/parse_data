
import pandas as pd
import json
from predictobstacle import PredictObstacle
from predictobstacle import SyncPredictObstacle
import queue

data_path = "/Users/panjiqing/Desktop/licode/data/predict_data/_viz_prediction_pred_obstacles.csv"

# data = pd.read_csv(data_path ,  error_bad_lines=False)
# print(data)

with open(data_path, 'r',encoding='utf-8-sig') as f:
    # 循环每行
    label_list = []
    for line in f:
        if line != '_viz_prediction_pred_obstacles\n':
            # print(json.loads(line)["markers"])
            data = json.loads(line)["markers"]
            if len(data) > 0:
                syncobs = SyncPredictObstacle(3)
                for obs in data:
                    pred_obs = PredictObstacle(obs)
                    pred_obs.get_id_time()
                    if pred_obs.id_time == None :
                        del pred_obs
                        continue
                    else:
                        syncobs.add_predict_obs(pred_obs)
                    print(pred_obs.id)
                    print('time:' , pred_obs.id_time)
                    # print('timestamp:' , pred_obs.timestamp)
                    # if predobs.label not in label_list:
                    # if len(predobs.id) ==  0 :
                    #     continue
                    # print(predobs.id)

                    # id , id_time= predobs.id.rsplit("_",1)
                    # print("id :" , id)
                    # if id_time in ['1s' , '2s' , '3s']:
                    #     print(id , id_time)
                if syncobs.sync_pred_obs_one != None: 
                    syncobs.get_sync_timestamp()
                    syncobs.get_sync_id()
                    print('sync timestamp:' ,syncobs.sync_timestamp,syncobs.sync_id)
                    print('syncobs finish',syncobs.sync_pred_obs_one)
                         
                        # print("labels :" , predobs.label)
                        #  = queue.Queue()      
                        # print(predobs.timestamp)
            # print(line)

