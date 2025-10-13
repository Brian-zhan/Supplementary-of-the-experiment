import os
import pandas as pd
import re
from statistics import mean

# 檢查閾值設定
inoc_stim_interval_thres = 0.1 #有發生的刺激，刺激預期時間最小長度（秒）
non_inoc_stim_interval_thres = 0.01 #未發生的刺激，刺激預期時間最大長度（秒）

# 輸出檔名都是all_listed_開頭的

psychopy_filename_str_array = [i for i in sorted([f for f in os.listdir('.') if f.endswith('.csv') and not f.startswith("all_")])]

demog_lookup = {1:'age', 2:'sex', 3:'height(cm)', 4:'bloodType', 5:'highestDegree'}
polperfs_lookup = {0:'iden', 1:'polfuture', 2:'polspec', 3:'partychoose'}

dummy_map_demog = {
    'sex': {
        '男性': 1,
        '女性': 0,
        '不方便透露': 2,
    },
    'bloodType': {
        'A': 0,
        'B': 1,
        'AB': 2,
        'O': 3,
    },
    'highestDegree': {
        '小學': 0,
        '國中': 1,
        '五專': 2,
        '高中': 3,
        '學士': 4,
        '碩士': 5,
        '博士': 6,
    }
}
dummy_map_polperfs = {
    'iden': {
        '台灣人': 0,
        '中國人': 1,
        '都是': 2,
    },
    'polfuture': {
        '儘快統一': 0,
        '儘快獨立': 1,
        '維持現狀，以後走向統一': 2,
        '維持現狀，以後走向獨立': 3,
        '維持現狀，看情形再決定獨立或統一': 4,
        '永遠維持現狀': 5,
    },
    'partychoose': {
        '國民黨': 0,
        '民進黨': 1,
    }
}

counterbalance_order = [
    [1,2,24,3,23,4,22,5,21,6,20,7,19,8,18,9,17,10,16,11,15,12,14,13],
    [2,3,1,4,24,5,23,6,22,7,21,8,20,9,19,10,18,11,17,12,16,13,15,14],
    [3,4,2,5,1,6,24,7,23,8,22,9,21,10,20,11,19,12,18,13,17,14,16,15],
    [4,5,3,6,2,7,1,8,24,9,23,10,22,11,21,12,20,13,19,14,18,15,17,16],
    [5,6,4,7,3,8,2,9,1,10,24,11,23,12,22,13,21,14,20,15,19,16,18,17],
    [6,7,5,8,4,9,3,10,2,11,1,12,24,13,23,14,22,15,21,16,20,17,19,18],
    [7,8,6,9,5,10,4,11,3,12,2,13,1,14,24,15,23,16,22,17,21,18,20,19],
    [8,9,7,10,6,11,5,12,4,13,3,14,2,15,1,16,24,17,23,18,22,19,21,20],
    [9,10,8,11,7,12,6,13,5,14,4,15,3,16,2,17,1,18,24,19,23,20,22,21],
    [10,11,9,12,8,13,7,14,6,15,5,16,4,17,3,18,2,19,1,20,24,21,23,22],
    [11,12,10,13,9,14,8,15,7,16,6,17,5,18,4,19,3,20,2,21,1,22,24,23],
    [12,13,11,14,10,15,9,16,8,17,7,18,6,19,5,20,4,21,3,22,2,23,1,24],
    [13,14,12,15,11,16,10,17,9,18,8,19,7,20,6,21,5,22,4,23,3,24,2,1],
    [14,15,13,16,12,17,11,18,10,19,9,20,8,21,7,22,6,23,5,24,4,1,3,2],
    [15,16,14,17,13,18,12,19,11,20,10,21,9,22,8,23,7,24,6,1,5,2,4,3],
    [16,17,15,18,14,19,13,20,12,21,11,22,10,23,9,24,8,1,7,2,6,3,5,4],
    [17,18,16,19,15,20,14,21,13,22,12,23,11,24,10,1,9,2,8,3,7,4,6,5],
    [18,19,17,20,16,21,15,22,14,23,13,24,12,1,11,2,10,3,9,4,8,5,7,6],
    [19,20,18,21,17,22,16,23,15,24,14,1,13,2,12,3,11,4,10,5,9,6,8,7],
    [20,21,19,22,18,23,17,24,16,1,15,2,14,3,13,4,12,5,11,6,10,7,9,8],
    [21,22,20,23,19,24,18,1,17,2,16,3,15,4,14,5,13,6,12,7,11,8,10,9],
    [22,23,21,24,20,1,19,2,18,3,17,4,16,5,15,6,14,7,13,8,12,9,11,10],
    [23,24,22,1,21,2,20,3,19,4,18,5,17,6,16,7,15,8,14,9,13,10,12,11],
    [24,1,23,2,22,3,21,4,20,5,19,6,18,7,17,8,16,9,15,10,14,11,13,12]
]
counterbalance_len = len(counterbalance_order)
we_correct_answer_lookup = {
    '000-1.png': 0,
    '000-2.png': 0,
    '000-3.png': 0,
    '001-1.png': 6,
    '001-2.png': 6,
    '001-3.png': 6,
    '010-1.png': 0,
    '010-2.png': 0,
    '010-3.png': 0,
    '011-1.png': 6,
    '011-2.png': 6,
    '011-3.png': 6,
    '100-1.png': 0,
    '100-2.png': 0,
    '100-3.png': 0,
    '101-1.png': 0, #曾經出錯
    '101-2.png': 6,
    '101-3.png': 6,
    '110-1.png': 0,
    '110-2.png': 0,
    '110-3.png': 0,
    '111-1.png': 6,
    '111-2.png': 6,
    '111-3.png': 6
}

all_results = []
avg_results = []
layered_results = []
all_result_categorized = []

def parse_button_string(s):
    """
    把像 "[0]", "[1]", "[1,0]", "[0,0]", "[1,1]" 這類字串轉成對應整數。
    規則：
    1. 找不到時 fallback 為把所有擷取到的數字做 sum()。
    2. 若 s 為 None/NaN/空字串，回傳 None。
    """
    if s is None:
        return None
    # 確保是字串
    s = str(s).strip()
    if s == "":
        return None

    # 抽出字串中所有的整數（保留順序），例如 "[1,0]" -> ['1','0']
    nums = re.findall(r'-?\d+', s)
    if not nums:
        return None

    # 轉成整數 tuple（用來做 mapping key）
    tup = tuple(int(n) for n in nums)

    # fallback: 如果是常見二元或單元，直接返回 sum，確保型別為 int
    try:
        return int(sum(tup))
    except Exception:
        return None

def process_buttons_pressed(df, row_index, mouse_name):
    left_button_name = f"{mouse_name}.leftButton"
    mid_button_name = f"{mouse_name}.midButton"
    right_button_name = f"{mouse_name}.rightButton"
    left_button_press_amount = parse_button_string(df.loc[row_index, left_button_name])
    mid_button_press_amount = parse_button_string(df.loc[row_index, mid_button_name])
    right_button_press_amount = parse_button_string(df.loc[row_index, right_button_name])
    try:
        total_button_press_amount = left_button_press_amount + mid_button_press_amount + right_button_press_amount
    except:
        raise RuntimeError("加總出問題囉，要出事了！")
    return left_button_press_amount, mid_button_press_amount, right_button_press_amount, total_button_press_amount

def get_buttons_pressed_status(df, start_label_name, stop_label_name, mouse_name):
    started_row_index = df[start_label_name].dropna().index[0]
    stopped_row_index = df[stop_label_name].dropna().index[0]
    if started_row_index == stopped_row_index:
        row_index = stopped_row_index
    else:
        print(f"警告：{start_label_name}和{stop_label_name}的索引不一樣！強制使用{start_label_name}")
        row_index = started_row_index
    buttons = process_buttons_pressed(df, row_index, mouse_name)
    return buttons

# 以上是E-Prime，現在來處理PsychoPy  
# 不是哪來的E-Prime  
for idx, filename_str in enumerate(psychopy_filename_str_array):
    try:
        df = pd.read_csv(filename_str)

        # 取 participant
        subj = df['participant'].iloc[0]
        print(f"解析受試者{subj}的資料中...",end="")

        part_cb_index = (subj - 1) % counterbalance_len
        raw_order = counterbalance_order[part_cb_index]
        trial_order = [i-1 for i in raw_order]

        if subj < 1:
            raise ValueError(f"WTF我們拿到了受試者號碼{subj}")

        inoculation_switch = 1 if subj % 2 == 1 else 0

        # 處理 intro
        intro_start_label_name = 'Introduction.started'
        intro_stop_label_name = 'Introduction.stopped'
        intro_started = df[intro_start_label_name].dropna().iloc[0]
        intro_stopped = df[intro_stop_label_name].dropna().iloc[0]
        intro_duration = intro_stopped - intro_started
        intro_buttons_pressed_status = get_buttons_pressed_status(df, intro_start_label_name, intro_stop_label_name, "mouse1")

        # 處理 Demographic form
        demog_started = df['Demographic_Form.started'].dropna().iloc[0]
        demog_stopped = df['Demographic_Form.stopped'].dropna().iloc[0]
        demog_duration = demog_stopped - demog_started
        demog_data = {}
        for _, row in df.iterrows():
            idx_val = row.get('demog_form.index', None)
            resp_val = row.get('demog_form.response', None)
            rt_val = row.get('demog_form.rt', None)

            if idx_val in demog_lookup:
                key_name = demog_lookup.get(idx_val, idx_val)  # 直接替換成文字

                # 先映射response值，如果有對應映射表才轉換，沒有就保留原值
                dummy_val = resp_val
                if key_name in dummy_map_demog:
                    dummy_val = dummy_map_demog[key_name].get(resp_val, None)  # 找不到時可回傳 None 或其他預設值

                if key_name in demog_data:
                    print(f"⚠ 警告：demog_form.index {idx_val}（{key_name}）出現重複")
                demog_data[key_name] = {
                    'response': dummy_val,
                    'rt': rt_val
                }
        demog_fill_finished = df['pre_indicator_3.stopped'].dropna().iloc[0]
        demog_rt1st = demog_fill_finished - demog_started
        demog_send_delay = demog_stopped - demog_fill_finished
        demog_data["demog_buttons"] = process_buttons_pressed(df, df["mouse2.leftButton"].dropna().index[0],"mouse2")

        # 處理 ino_intro_duration
        ino_intro_start_label_name = 'Ino_Intro.started'
        ino_intro_stop_label_name = 'Ino_Intro.stopped'
        ino_intro_started = df[ino_intro_start_label_name].dropna().iloc[0]
        ino_intro_stopped = df[ino_intro_stop_label_name].dropna().iloc[0]
        ino_intro_duration = ino_intro_stopped - ino_intro_started
        ino_intro_buttons_pressed_status = get_buttons_pressed_status(df, ino_intro_start_label_name, ino_intro_stop_label_name, "mouse69")

        # 計算 ino_duration(Ino/NonIno)
        ino_start_label_name = 'Inoculation.started'
        ino_stop_label_name = 'Inoculation.stopped'
        non_ino_start_label_name = 'NonInoculation.started'
        non_ino_stop_label_name = 'NonInoculation.stopped'
        ino_started = df[ino_start_label_name].dropna().iloc[0]
        ino_stopped = df[ino_stop_label_name].dropna().iloc[0]
        non_ino_started = df[non_ino_start_label_name].dropna().iloc[0]
        non_ino_stopped = df[non_ino_stop_label_name].dropna().iloc[0]
        ino_interval = ino_stopped - ino_started
        non_ino_interval = non_ino_stopped - non_ino_started
        # 一些條件檢查，嗯
        if ino_interval < 0:
            print(f"[受試者{subj}] 警告：接受接種的時間區段秒數為{ino_interval}，但這不應該發生")
        if non_ino_interval < 0:
            print(f"[受試者{subj}] 警告：不接受接種的時間區段秒數為{non_ino_interval}，但這不應該發生")
        if inoculation_switch == 1:
            if (ino_interval > non_ino_interval) and ino_interval > inoc_stim_interval_thres and non_ino_interval < non_inoc_stim_interval_thres:
                ino_routine_duration = ino_interval # 檢查通過
                ino_routine_buttons_pressed_status = get_buttons_pressed_status(df, ino_start_label_name, ino_stop_label_name, "mouse4")
            else:
                print(f"[受試者{subj}] 警告：接受接種的時間區段秒數為{ino_interval}，但這不應該發生")
        elif inoculation_switch == 0:
            if (non_ino_interval > ino_interval) and non_ino_interval > inoc_stim_interval_thres and ino_interval < non_inoc_stim_interval_thres:
                ino_routine_duration = non_ino_interval # 檢查通過
                ino_routine_buttons_pressed_status = get_buttons_pressed_status(df, non_ino_start_label_name, non_ino_stop_label_name, "mouse5")
            else:
                print(f"[受試者{subj}] 警告：未接受接種的時間區段秒數為{non_ino_interval}，但這不應該發生")
        else:
            print("wtf(遇到了很靠北嚴重的問題)")
        # 此時會獲得ino_routine_duration跟ino_routine_buttons_pressed_status
        
        # 處理start_of_practice
        sop_start_label_name = 'Start_Of_Practice.started'
        sop_stop_label_name = 'Start_Of_Practice.stopped'
        sop_started = df[sop_start_label_name].dropna().iloc[0]
        sop_stopped = df[sop_stop_label_name].dropna().iloc[0]
        sop_duration = sop_stopped - sop_started
        sop_buttons_pressed_status = get_buttons_pressed_status(df, sop_start_label_name, sop_stop_label_name, "mouse6")

        # 處理end_of_practice
        eop_start_label_name = 'End_Of_Practice.started'
        eop_stop_label_name = 'End_Of_Practice.stopped'
        eop_started = df[eop_start_label_name].dropna().iloc[0]
        eop_stopped = df[eop_stop_label_name].dropna().iloc[0]
        eop_duration = eop_stopped - eop_started
        eop_buttons_pressed_status = get_buttons_pressed_status(df,eop_start_label_name, eop_stop_label_name, "mouse9")

        # ...我們最後再來處理這個

        # 處理end_of_main_trial      
        eomt_start_label_name = 'End_Of_Main_Trial.started'
        eomt_stop_label_name = 'End_Of_Main_Trial.stopped'
        eomt_started = df[eomt_start_label_name].dropna().iloc[0]
        eomt_stopped = df[eomt_stop_label_name].dropna().iloc[0]
        eomt_duration = eomt_stopped - eomt_started
        eomt_buttons_pressed_status = get_buttons_pressed_status(df,eomt_start_label_name, eomt_stop_label_name, "mouse10")

        # 處理 Political perfs form
        polperfs_started = df['Political_Prefs_Form.started'].dropna().iloc[0]
        polperfs_stopped = df['Political_Prefs_Form.stopped'].dropna().iloc[0]
        polperfs_duration = polperfs_stopped - polperfs_started
        polperfs_data = {}
        for _, row in df.iterrows():
            idx_val = row.get('PBF_form.index', None)
            resp_val = row.get('PBF_form.response', None)
            rt_val = row.get('PBF_form.rt', None)

            if idx_val in polperfs_lookup:
                key_name = polperfs_lookup.get(idx_val, idx_val)  # 直接替換成文字

                # 先映射response值，如果有對應映射表才轉換，沒有就保留原值
                dummy_val = resp_val
                if key_name in dummy_map_polperfs:
                    dummy_val = dummy_map_polperfs[key_name].get(resp_val, None)  # 找不到時可回傳 None 或其他預設值

                if key_name in polperfs_data:
                    print(f"⚠ PBF_form.index {idx_val}（{key_name}）出現重複")
                polperfs_data[key_name] = {
                    'response': dummy_val,
                    'rt': rt_val
                }
        polperfs_fill_finished = df['pre_indicator_2.stopped'].dropna().iloc[0]
        polperfs_rt1st = polperfs_fill_finished - polperfs_started
        polperfs_send_delay = polperfs_stopped - polperfs_fill_finished
        polperfs_data["polperfs_buttons"] = process_buttons_pressed(df, df["mouse3.leftButton"].dropna().index[0],"mouse3")

        #來吧...
        # 處理圖片刺激

        def picname_to_digits(picname):
            # 擷取前 3 個數字，例如 "000-1.png" -> "000"
            prefixs = picname.split("-")  # "000"
            prefix_head = prefixs[0]
            # 將字元轉成整數
            return [int(d) for d in prefix_head] + [int(prefixs[1].split(".")[0])]
        
        def check_picname(picname):
            match = re.match(r"^(\d{3})-(\d)\.png$", picname)
            if not match:
                return False  # 格式錯誤
            prefix, suffix = match.groups()
            # 驗證是否符合 000~111-1~3 範圍
            if any(int(d) > 1 for d in prefix) or not (1 <= int(suffix) <= 3):
                return False
            # input([int(d) for d in prefix])
            return True
        
        # 建立轉換函式
        def get_label(digits):
            part1 = "KMT" if digits[0] == 0 else "DPP"
            part2 = "True" if digits[1] == 0 else "False"
            part3 = "RealEmo" if digits[2] == 0 else "RevEmo"
            part4 = f"pic{digits[3]}"
            return f"{part1}_{part2}_{part3}_{part4}"
        
        # 建立轉換函式
        def get_label_avg(digits):
            part1 = "KMT" if digits[0] == 0 else "DPP"
            part2 = "True" if digits[1] == 0 else "False"
            part3 = "RealEmo" if digits[2] == 0 else "RevEmo"
            return f"{part1}_{part2}_{part3}"

        def sort_key(filename):
            # 把 "000-1.png" 拆成 (000, 1)
            match = re.match(r"(\d+)-(\d+)\.png", filename)
            if match:
                return (int(match.group(1)), int(match.group(2)))
            return (0, 0)  # 防呆

        def sort_key_avg(filename):
            # 把 "000-1.png" 拆成 (000, 1)
            match = re.match(r"(\d+)-avg", filename)
            if match:
                return (int(match.group(1)))
            return (0, 0)  # 防呆
        
        # 建立一個用來儲存圖片刺激結果的 dict：在這裡控制我們要納入哪些東西
        result = {}
        result_avg = {}
        stimuli_img_order_index = 1

        for idx_stim, row in df.iterrows():
            key = str(row['stim_picname'])
            key_avg = key.split("-")[0] + "-avg"
            if not check_picname(key):
                continue
            digits_all = picname_to_digits(key)
            if key not in result:
                result[key] = {'digits': digits_all, 'party': digits_all[0], 'isFake': digits_all[1], 'EmoFake': digits_all[2], 'stimuli_img_duration': None, 'stimuli_img_order': None, 'stimuli_img_mouse_press': None, 'tof_value': None, 'tof_rt': None, 'tof_mouse_press': None, 'tof_mouse_rt1st': None, 'tof_order': None, 'we_value': None, 'we_correct_ans': we_correct_answer_lookup[key], 'we_rt': None, 'we_mouse_press': None, 'we_mouse_rt1st': None, 'we_order': None, 'att_value': None, 'att_rt': None, 'att_mouse_press': None, 'att_mouse_rt1st': None, 'att_order': None}
            if key_avg not in result_avg:
                result_avg[key_avg] = {'digits': digits_all, 'party': digits_all[0], 'isFake': digits_all[1], 'EmoFake': digits_all[2], 'stimuli_img_duration': [], 'stimuli_img_mouse_press': [], 'tof_value': [], 'tof_rt': [], 'tof_mouse_press': [], 'tof_mouse_rt1st': [], 'we_rt': [], 'we_mouse_rt1st': [], 'att_value': [], 'att_rt': [], 'att_mouse_press': [], 'att_mouse_rt1st': []}
            #party: 0=KMT, 1=DPP
            #isfake: 0=True, 1=Manipulated
            #EmoFake: 0=normal(thumb+), 1=Manipulated(angry+)
            
            # 寫入圖片刺激總耗時
            if not result[key]['stimuli_img_duration']:
                stimuli_stopped = row.get('stimuli_img.stopped', None)
                stimuli_started = row.get('stimuli_img.started', None)
                if stimuli_started and stimuli_stopped:
                    stimuli_duration = stimuli_stopped - stimuli_started
                    result[key]['stimuli_img_duration'] = stimuli_duration
                    result_avg[key_avg]['stimuli_img_duration'].append(stimuli_duration)
                result[key]['stimuli_img_order'] = stimuli_img_order_index
                stimuli_img_order_index += 1
                stim_img_btn_press = process_buttons_pressed(df, idx_stim, "mouse7")
                result[key]['stimuli_img_mouse_press'] = stim_img_btn_press
                result_avg[key_avg]['stimuli_img_mouse_press'].append(stim_img_btn_press)
            # 寫入回應資訊耗時與取值
            switch = row['resp_switch']
            if switch == 1:
                result[key]['tof_value'] = row.get('true_or_false.response', None)
                result_avg[key_avg]['tof_value'].append(result[key]['tof_value'])
                tof_start = row.get('resp_mixed.started', None)
                tof_stop = row.get('resp_mixed.stopped', None)
                if tof_stop and tof_start:
                    result[key]['tof_rt'] = tof_stop - tof_start
                    result_avg[key_avg]['tof_rt'].append(result[key]['tof_rt'])
                result[key]['tof_mouse_press'] = process_buttons_pressed(df, idx_stim, "mouse8")
                result_avg[key_avg]['tof_mouse_press'].append(result[key]['tof_mouse_press'])
                result[key]['tof_mouse_rt1st'] = row.get('true_or_false.rt', None)
                result_avg[key_avg]['tof_mouse_rt1st'].append(result[key]['tof_mouse_rt1st'])
                tof_order_index = row.get('resp_main_loop.thisIndex', None)
                if tof_order_index != None:
                    result[key]['tof_order'] = int(tof_order_index)
            elif switch == 2:
                result[key]['we_value'] = int(row.get('which_emoji.response', None))
                we_start = row.get('resp_mixed.started', None)
                we_stop = row.get('resp_mixed.stopped', None)
                if we_stop and we_start:
                    result[key]['we_rt'] = we_stop - we_start
                    result_avg[key_avg]['we_rt'].append(result[key]['we_rt'])
                result[key]['we_mouse_press'] = process_buttons_pressed(df, idx_stim, "mouse8")
                result[key]['we_mouse_rt1st'] = row.get('which_emoji.rt', None)
                result_avg[key_avg]['we_mouse_rt1st'].append(result[key]['we_mouse_rt1st'])
                we_order_index = row.get('resp_main_loop.thisIndex', None)
                if we_order_index != None:
                    result[key]['we_order'] = int(we_order_index)
            elif switch == 3:
                result[key]['att_value'] = row.get('attitude.response', None)
                result_avg[key_avg]['att_value'].append(result[key]['att_value'])
                att_start = row.get('resp_mixed.started', None)
                att_stop = row.get('resp_mixed.stopped', None)
                if att_stop and att_start:
                    result[key]['att_rt'] = att_stop - att_start
                    result_avg[key_avg]['att_rt'].append(result[key]['att_rt'])
                result[key]['att_mouse_press'] = process_buttons_pressed(df, idx_stim, "mouse8")
                result_avg[key_avg]['att_mouse_press'].append(result[key]['att_mouse_press'])
                result[key]['att_mouse_rt1st'] = row.get('attitude.rt', None)
                result_avg[key_avg]['att_mouse_rt1st'].append(result[key]['att_mouse_rt1st'])
                att_order_index = row.get('resp_main_loop.thisIndex', None)
                if att_order_index != None:
                    result[key]['att_order'] = int(att_order_index)

        # 儲存所有結果的 dict(正常標準化輸出)
        output = {}
        output_all = {}

        output_all["participant"] = subj
        output_all["inoculation_switch"] = inoculation_switch

        #demographic data
        for idx, key_name in demog_lookup.items():  # 會照 lookup 的順序
            if key_name in demog_data:
                output_all[f"{key_name}_value"] = demog_data.get(key_name,{}).get('response')
                output_all[f"{key_name}_rt"] = demog_data.get(key_name,{}).get('rt')
        
        #political perference data
        for idx, key_name in polperfs_lookup.items():  # 會照 lookup 的順序
            if key_name in polperfs_data:
                output_all[f"{key_name}_value"] = polperfs_data.get(key_name,{}).get('response')
                output_all[f"{key_name}_rt"] = polperfs_data.get(key_name,{}).get('rt')

        output_all["Intro_rt"] = intro_duration
        output_all["Intro_LMousePress"], output_all["Intro_MMousePress"], output_all["Intro_RMousePress"], output_all["Intro_AllMousePress"] = intro_buttons_pressed_status

        output_all["Demog_rt"] = demog_duration #表單啟動至表單結束（正式送出）
        output_all["Demog_rt1st"] = demog_rt1st #表單啟動至初次完成表單
        output_all["Demog_delay"] = demog_send_delay #初次完成表單至表單結束（正式送出）
        output_all["Demog_LMousePress"], output_all["Demog_MMousePress"], output_all["Demog_RMousePress"], output_all["Demog_AllMousePress"] = demog_data["demog_buttons"]

        output_all["InoIntro_rt"] = ino_intro_duration
        output_all["InoIntro_LMousePress"], output_all["InoIntro_MMousePress"], output_all["InoIntro_RMousePress"], output_all["InoIntro_AllMousePress"] = ino_intro_buttons_pressed_status

        output_all["InoRoutine_rt"] = ino_routine_duration
        output_all["InoRoutine_LMousePress"], output_all["InoRoutine_MMousePress"], output_all["InoRoutine_RMousePress"], output_all["InoRoutine_AllMousePress"] = ino_routine_buttons_pressed_status

        output_all["SOP_rt"] = sop_duration
        output_all["SOP_LMousePress"], output_all["SOP_MMousePress"], output_all["SOP_RMousePress"], output_all["SOP_AllMousePress"] = sop_buttons_pressed_status

        output_all["EOP_rt"] = eop_duration
        output_all["EOP_LMousePress"], output_all["EOP_MMousePress"], output_all["EOP_RMousePress"], output_all["EOP_AllMousePress"] = eop_buttons_pressed_status

        output_all["EOMT_rt"] = eomt_duration
        output_all["EOMT_LMousePress"], output_all["EOMT_MMousePress"], output_all["EOMT_RMousePress"], output_all["EOMT_AllMousePress"] = eomt_buttons_pressed_status

        output_all["PoPerfs_rt"] = polperfs_duration #表單啟動至表單結束（正式送出）
        output_all["PoPerfs_rt1st"] = polperfs_rt1st #表單啟動至初次完成表單
        output_all["PoPerfs_delay"] = polperfs_send_delay #初次完成表單至表單結束（正式送出）
        output_all["PoPerfs_LMousePress"], output_all["PoPerfs_MMousePress"], output_all["PoPerfs_RMousePress"], output_all["PoPerfs_AllMousePress"] = polperfs_data["polperfs_buttons"]

        # 假設 result 是你的大字典
        sorted_result = dict(sorted(result.items(), key=lambda item: sort_key(item[0])))
        if not result == sorted_result:
            print("警告：排序轉換檢查未通過，請檢查腳本")
        
        for key, entry in sorted_result.items():
            label = get_label(entry['digits'])
            for field, value in entry.items():
                if field == 'digits':  # 跳過 digits
                    continue
                if "mouse_press" in field:
                    lmouse_field_name = field.replace("mouse_press", "LMousePress")
                    mmouse_field_name = field.replace("mouse_press", "MMousePress")
                    rmouse_field_name = field.replace("mouse_press", "RMousePress")
                    allmouse_field_name = field.replace("mouse_press", "AllMousePress")
                    output_all[f"{label}_{lmouse_field_name}"], output_all[f"{label}_{mmouse_field_name}"], output_all[f"{label}_{rmouse_field_name}"], output_all[f"{label}_{allmouse_field_name}"] = value
                    continue
                if field == 'tof_value':
                    output_all[f"{label}_{field}"] = value
                    output_all[f"{label}_tof_dist"] = abs(value-5)
                    continue
                if field == 'we_value':
                    output_all[f"{label}_{field}"] = value
                    output_all[f"{label}_we_isCorrect"] = 1 if value == entry["we_correct_ans"] else 0
                    continue
                if field == 'att_value':
                    output_all[f"{label}_{field}"] = value
                    output_all[f"{label}_att_dist"] = abs(value-5.5)
                    continue
                output_all[f"{label}_{field}"] = value

        output_all_avg = {}

        output_all_avg["participant"] = subj
        output_all_avg["inoculation_switch"] = inoculation_switch

        #demographic data
        for idx, key_name in demog_lookup.items():  # 會照 lookup 的順序
            if key_name in demog_data:
                output_all_avg[f"{key_name}_value"] = demog_data.get(key_name,{}).get('response')
                output_all_avg[f"{key_name}_rt"] = demog_data.get(key_name,{}).get('rt')
        
        #political perference data
        for idx, key_name in polperfs_lookup.items():  # 會照 lookup 的順序
            if key_name in polperfs_data:
                output_all_avg[f"{key_name}_value"] = polperfs_data.get(key_name,{}).get('response')
                output_all_avg[f"{key_name}_rt"] = polperfs_data.get(key_name,{}).get('rt')

        output_all_avg["Intro_rt"] = intro_duration
        output_all_avg["Intro_LMousePress"], output_all_avg["Intro_MMousePress"], output_all_avg["Intro_RMousePress"], output_all_avg["Intro_AllMousePress"] = intro_buttons_pressed_status

        output_all_avg["Demog_rt"] = demog_duration #表單啟動至表單結束（正式送出）
        output_all_avg["Demog_rt1st"] = demog_rt1st #表單啟動至初次完成表單
        output_all_avg["Demog_delay"] = demog_send_delay #初次完成表單至表單結束（正式送出）
        output_all_avg["Demog_LMousePress"], output_all_avg["Demog_MMousePress"], output_all_avg["Demog_RMousePress"], output_all_avg["Demog_AllMousePress"] = demog_data["demog_buttons"]

        output_all_avg["InoIntro_rt"] = ino_intro_duration
        output_all_avg["InoIntro_LMousePress"], output_all_avg["InoIntro_MMousePress"], output_all_avg["InoIntro_RMousePress"], output_all_avg["InoIntro_AllMousePress"] = ino_intro_buttons_pressed_status

        output_all_avg["InoRoutine_rt"] = ino_routine_duration
        output_all_avg["InoRoutine_LMousePress"], output_all_avg["InoRoutine_MMousePress"], output_all_avg["InoRoutine_RMousePress"], output_all_avg["InoRoutine_AllMousePress"] = ino_routine_buttons_pressed_status

        output_all_avg["SOP_rt"] = sop_duration
        output_all_avg["SOP_LMousePress"], output_all_avg["SOP_MMousePress"], output_all_avg["SOP_RMousePress"], output_all_avg["SOP_AllMousePress"] = sop_buttons_pressed_status

        output_all_avg["EOP_rt"] = eop_duration
        output_all_avg["EOP_LMousePress"], output_all_avg["EOP_MMousePress"], output_all_avg["EOP_RMousePress"], output_all_avg["EOP_AllMousePress"] = eop_buttons_pressed_status

        output_all_avg["EOMT_rt"] = eomt_duration
        output_all_avg["EOMT_LMousePress"], output_all_avg["EOMT_MMousePress"], output_all_avg["EOMT_RMousePress"], output_all_avg["EOMT_AllMousePress"] = eomt_buttons_pressed_status

        output_all_avg["PoPerfs_rt"] = polperfs_duration #表單啟動至表單結束（正式送出）
        output_all_avg["PoPerfs_rt1st"] = polperfs_rt1st #表單啟動至初次完成表單
        output_all_avg["PoPerfs_delay"] = polperfs_send_delay #初次完成表單至表單結束（正式送出）
        output_all_avg["PoPerfs_LMousePress"], output_all_avg["PoPerfs_MMousePress"], output_all_avg["PoPerfs_RMousePress"], output_all_avg["PoPerfs_AllMousePress"] = polperfs_data["polperfs_buttons"]

        # 假設 result_avg 是你的大字典
        sorted_result_avg = dict(sorted(result_avg.items(), key=lambda item: sort_key_avg(item[0])))
        if not result_avg == sorted_result_avg:
            print("警告：排序轉換檢查未通過，請檢查腳本")
        
        for key, entry in sorted_result_avg.items():
            label = get_label_avg(entry['digits'])
            for field, value in entry.items():
                if field == 'digits':  # 跳過 digits
                    continue
                if "mouse_press" in field:
                    lmouse_field_name = field.replace("mouse_press", "LMousePress")
                    mmouse_field_name = field.replace("mouse_press", "MMousePress")
                    rmouse_field_name = field.replace("mouse_press", "RMousePress")
                    allmouse_field_name = field.replace("mouse_press", "AllMousePress")
                    avg_mouse_press = tuple(
                        sum(col) / len(col)
                        for col in zip(*value)
                    )
                    output_all_avg[f"{label}_{lmouse_field_name}"], output_all_avg[f"{label}_{mmouse_field_name}"], output_all_avg[f"{label}_{rmouse_field_name}"], output_all_avg[f"{label}_{allmouse_field_name}"] = avg_mouse_press
                    continue
                if type(value) == list:
                    output_all_avg[f"{label}_{field}"] = mean(value)
                    if field == 'tof_value':
                        output_all_avg[f"{label}_tof_dist"] = mean([abs(value_unit-5) for value_unit in value])
                    if field == 'att_value':
                        output_all_avg[f"{label}_att_dist"] = mean([abs(value_unit-5.5) for value_unit in value])
                    continue
                output_all_avg[f"{label}_{field}"] = value

        output_all_layered = {1: {}, 2: {}, 3: {}}

        for key, entry in output_all.items():
            matched_layer = None
            for layer in (1, 2, 3):
                marker = f"_pic{layer}_"
                if marker in key:
                    matched_layer = layer
                    new_key = key.replace(marker, "_")
                    output_all_layered[layer][new_key] = entry
                    break
            if matched_layer is None:
                # 不含任何 _pic1_, _pic2_, _pic3_，塞進所有 layer
                for layer in (1, 2, 3):
                    output_all_layered[layer][key] = entry
        
        # 寫入all_result_categorized的預備資料
        base_data = {k: v for k, v in output_all.items() if not any(tag in k for tag in ["KMT_", "DPP_"])}

        # 暫存用 → key: (party, fake, emo, pic), value: dict
        stim_groups = {}

        for key, value in output_all.items():
            # print(f"處理參與者{subj} 鍵{key}")
            if key.startswith("KMT_") or key.startswith("DPP_"):
                try:
                    A, B, C, D, rest_key = key.split("_", 4)
                    stim_party = 0 if A == "KMT" else 1
                    stim_isFake = 0 if B == "True" else 1
                    stim_EmoFake = 0 if C == "RealEmo" else 1
                    stim_picNum = int(D.replace("pic", ""))

                    stim_key = (stim_party, stim_isFake, stim_EmoFake, stim_picNum)

                    if stim_key not in stim_groups:
                        stim_groups[stim_key] = {
                            "stim_party": stim_party,
                            "stim_isFake": stim_isFake,
                            "stim_EmoFake": stim_EmoFake,
                            "stim_picNum": stim_picNum
                        }
                    
                    stim_groups[stim_key][rest_key] = value

                except Exception as e:
                    print(f"⚠ 無法解析 {key}: {e}")
            
        # 合併 base_data + 每個 stim 組
        for stim_data in stim_groups.values():
            new_entry = base_data.copy()
            new_entry.update(stim_data)
            all_result_categorized.append(new_entry)

        # output_all: 所有基礎資料的匯出：逐參與者
        # output_all_avg: 所有基礎資料的匯出：求平均值
        # output_all_layered: 所有基礎資料的匯出：拆分三次數據至三個相同受試者
        
        all_results.append(output_all)
        avg_results.append(output_all_avg)
        for layer in sorted(output_all_layered.keys()):
            layered_results.append(output_all_layered[layer])
    
    except Exception as e:
        print(f"[受試者{subj}]錯誤發生：{e}，將直接跳過！")
    
    finally:
        print("成功！")

# 合併所有人資料，輸出一次
print("嘗試寫入all_listed_main...")
all_data_df = pd.concat([pd.DataFrame([r]) for r in all_results], ignore_index=True)
all_data_df.to_csv('all_listed_main.csv', index=False)

print("嘗試寫入all_avg_listed_main...")
all_avg_data_df = pd.concat([pd.DataFrame([r]) for r in avg_results], ignore_index=True)
all_avg_data_df.to_csv('all_avg_listed_main.csv', index=False)

print("嘗試寫入all_layered_listed_main...")
all_layered_data_df = pd.concat([pd.DataFrame([r]) for r in layered_results], ignore_index=True)
all_layered_data_df.to_csv('all_layered_listed_main.csv', index=False)

# print(len(all_result_categorized))

print("嘗試寫入all_data_categorized_main...")
all_data_categorized_df = pd.concat([pd.DataFrame([r]) for r in all_result_categorized], ignore_index=True)
all_data_categorized_df.to_csv('all_data_categorized_main.csv', index=False)

print("✅ 搞定，現在給我滾去睡覺！😡😡")
exit() #後面是排序用的舊程式，用不到

# 1. 定義要放在最前面的基本欄位
base_cols = ['Participant', 'Experimenter', 'Platform', 'intro_duration', 'eop_duration', 'combined_middelay']

# 2. 定義我們希望集中在一起的後綴順序
suffixes = ['_dist', '_offset', '_orient', '_is5', '_is10', '_off5', '_off10']

# 3. 找出所有以 '_value' 結尾的欄位，保留它們原本在 CSV 中的先後順序
value_cols = [col for col in combined_df.columns if col.endswith('_value')]

# 4. 輔助函式：篩選出所有帶有特定後綴的欄位
def cols_with_suffix(all_cols, suffix):
    return [col for col in all_cols if col.endswith(suffix)]

# 5. 開始組成新的欄位順序
ordered_cols = base_cols.copy()

for suffix in suffixes:
    # 先找出目前 DataFrame 中，所有帶這個 suffix 的欄位
    matched = cols_with_suffix(combined_df.columns, suffix)

    # 依照 value_cols 裡前綴的順序排列這些 matched 欄位
    # 先取得 value_cols 裡每一個欄位的 prefix（去掉 '_value'）
    prefixes = [col[:-6] for col in value_cols]  # 例如 'black3_value' → 'black3'

    # 只保留那些 prefix + suffix 實際出現在 matched 裡的 prefix，維持 value_cols 的相對前後順序
    matching_prefixes = [p for p in prefixes if (p + suffix) in matched]

    # 按照 matching_prefixes 的順序，組出完整欄位名稱並依序加入 ordered_cols
    for p in matching_prefixes:
        ordered_cols.append(p + suffix)

# 6. 最後把「不在 ordered_cols 之中的其他欄位」放到最尾端
remaining = [col for col in combined_df.columns if col not in ordered_cols]
ordered_cols.extend(remaining)

# 7. 重新套用欄位順序
reordered_df = combined_df[ordered_cols]

# 8. 輸出成新的 CSV
reordered_df.to_csv('all_data_reordered_dist.csv', index=False)