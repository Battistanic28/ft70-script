import pandas as pd
from itertools import zip_longest

adms10_columns = [
    '#', 'PRIORITY CHANNEL', 'Rx FREQ', 'Tx FREQ', 'OFFSET FREQ', 'OFFSET DIR', 'AUTO MODE', 'OPERATING MODE',
    'AMS', 'DIG/ANALOG', 'NAME', 'TONE MODE', 'CTCSS FREQ', 'DCS CODE', 'DCS POLARITY', 'USER CTCSS',
    'Tx POWER', 'SKIP', 'AUTO STEP', 'STEP', 'TAG', 'MEMOY MASK', 'ATT', 'S METER SQL', 'BELL', 'HALF DEV', 'CLOCK SHIFT',
    'BANK 1', 'BANK 2', 'BANK 3', 'BANK 4', 'BANK 5','BANK 7', 'BANK 8', 'BANK 9', 'BANK 10', 'BANK 11','BANK 12', 'BANK 13',
    'BANK 14', 'BANK 15', 'BANK 16','BANK 17', 'BANK 18', 'BANK 19', 'BANK 20', 'BANK 21', 'BANK 12', 'BANK 23', 'BANK 24',
    'COMMENT' 'BLANK'
    ]

# column_transfer_pattern = [0,'priority channel',1,2,3,4,'auto mode',5,'AMS','Dig/Analog',15,7,8,9,
#                            'DGS Polarity',10,11,12,'auto step',13,
#                         ]

df_input = pd.read_csv('data.csv', on_bad_lines='skip', header=None)
df_output = pd.DataFrame();

columns_to_transfer = [0,1,2,3,4,5,15,7,8,9,10,11,12,13]

# Clean channel description data
df_input[15] = df_input[15].apply(lambda x: x.split(' - ', 1)[-1])

# Transfer existing data
df_output = df_input.loc[:, columns_to_transfer]

# Hardcode missing data
df_output.insert(1, 'PRIORITY CHANNEL', 'OFF');
df_output.insert(6, 'AUTO MODE', 'ON');
df_output.insert(8, 'AMS', 'ON');
df_output.insert(9, 'DIG/ANALOG', 'ANALOG');
df_output.insert(14, 'DCS POLARITY', 'RX Normal TX Normal');
df_output.insert(18, 'AUTO STEP', 'ON');

# Rename columns
column_dict = dict(zip_longest(df_output.columns, adms10_columns))
renamed_df_output = df_output.rename(column_dict, axis='columns')

# Print output
print(renamed_df_output)
