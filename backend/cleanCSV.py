import pandas as pd

# Load CPU data
cpu_data = pd.read_csv('backend/dataset/CPUData.csv')
# Load Cooler data
cooler_data = pd.read_csv('backend/dataset/CPUCoolerData.csv')
# Load Case data
case_data = pd.read_csv('backend/dataset/CaseData.csv')
# Load GPU data
gpu_data = pd.read_csv('backend/dataset/GPUData.csv')
# Load HDD data
hdd_data = pd.read_csv('backend/dataset/HDDData.csv')
# Load Monitor data
monitor_data = pd.read_csv('backend/dataset/MonitorData.csv')
# Load Motherboard data
motherboard_data = pd.read_csv('backend/dataset/MotherboardData.csv')
# Load PSU data
psu_data = pd.read_csv('backend/dataset/PSUData.csv')
# Load RAM data
ram_data = pd.read_csv('backend/dataset/RAMData.csv')
# Load SSD data
ssd_data = pd.read_csv('backend/dataset/SSDData.csv')

#Remove duplicate
cpu_data.drop_duplicates(inplace=True)
gpu_data.drop_duplicates(inplace=True)
psu_data.drop_duplicates(inplace=True)
ram_data.drop_duplicates(inplace=True)
hdd_data.drop_duplicates(inplace=True)
monitor_data.drop_duplicates(inplace=True)
motherboard_data.drop_duplicates(inplace=True)
cooler_data.drop_duplicates(inplace=True)
case_data.drop_duplicates(inplace=True)

#Remove 50% and below
threshold = len(cpu_data) * 0.5
cpu_data_cleaned = cpu_data.dropna(axis=1, thresh=threshold)
cpu_data_cleaned.to_csv('backend/dataset/cleaned_cpu_data.csv', index=False)

threshold = len(ram_data) * 0.5
ram_data_cleaned = ram_data.dropna(axis=1, thresh=threshold)
ram_data_cleaned.to_csv('backend/dataset/cleaned_ram_data.csv', index=False)

threshold = len(psu_data) * 0.5
psu_data_cleaned = psu_data.dropna(axis=1, thresh=threshold)
psu_data_cleaned.to_csv('backend/dataset/cleaned_psu_data.csv', index=False)

threshold = len(ssd_data) * 0.5
ssd_data_cleaned = ssd_data.dropna(axis=1, thresh=threshold)
ssd_data_cleaned.to_csv('backend/dataset/cleaned_ssd_data.csv', index=False)

threshold = len(hdd_data) * 0.5
hdd_data_cleaned = hdd_data.dropna(axis=1, thresh=threshold)
hdd_data_cleaned.to_csv('backend/dataset/cleaned_hdd_data.csv', index=False)

threshold = len(monitor_data) * 0.5
monitor_data_cleaned = monitor_data.dropna(axis=1, thresh=threshold)
monitor_data_cleaned.to_csv('backend/dataset/cleaned_monitor_data.csv', index=False)

threshold = len(motherboard_data) * 0.5
motherboard_data_cleaned = motherboard_data.dropna(axis=1, thresh=threshold)
motherboard_data_cleaned.to_csv('backend/dataset/cleaned_motherboard_data.csv', index=False)

threshold = len(gpu_data) * 0.5
gpu_data_cleaned = gpu_data.dropna(axis=1, thresh=threshold)
gpu_data_cleaned.to_csv('backend/dataset/cleaned_gpu_data.csv', index=False)

threshold = len(cooler_data) * 0.5
cooler_data_cleaned = cooler_data.dropna(axis=1, thresh=threshold)
cooler_data_cleaned.to_csv('backend/dataset/cleaned_cooler_data.csv', index=False)

threshold = len(case_data) * 0.5
case_data_cleaned = case_data.dropna(axis=1, thresh=threshold)
case_data_cleaned.to_csv('backend/dataset/cleaned_case_data.csv', index=False)

print("Cleaned CSV successfully!")