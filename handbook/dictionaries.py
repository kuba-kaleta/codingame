val_x = ['X_', 'Y_','Z_','X_','Y_']
col_x = ['test1_', 'test2_', 'test3_', 'test4_', 'test5_']
encoder = ['X_test1', 'Y_test2','Z_test3','Y_test4','Y_test0']

# tworzenie slownika (dictionary) (mozesz wpisac recznie)
val_col = {}
for idx, x in enumerate(val_x):
    val_col[x] = col_x[idx]
print("val_col: ", val_col) # {'XO_': 'BOE_S', 'X1_': 'MIGRATION_CDE', 'X2_': 'PKD', 'X3_': 'PKD_SECTOR', 'X4_': 'SUB_SEGMENT'}
# odwolanie do elementu: print(val_col['XO_']) ==> 'BOE_S'

for idx, x in enumerate(encoder):
    encoder[idx] = val_col[x[:2]] + x[2:]
print("OH_encoder_col: ", encoder) # OH_encoder_col:  ['BOE_test1', 'MIGRATION_test2', 'PKD_test3', 'PKD_SECTOR_test4', 'SUB_SEGMENT_test']
