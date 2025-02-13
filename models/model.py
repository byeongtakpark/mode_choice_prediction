# import pandas as pd
# import numpy as np
# import xlogit
# from sklearn.metrics import accuracy_score




# class MultinomialLogitModel():
#     def __init__(self, df):
#         self.df = self.preprocess_data(df)

#     def MultinomialLogitModel(df_X_train, df_y_train):
#         # Concatenate feature data (X) and target data (y) into one DataFrame
#         df = pd.concat([df_X_train, df_y_train], axis=1)

#         # Add an ID column for identifying each individual choice
#         df['id'] = np.arange(len(df))

#         # Rename 'totaltime_auto' and 'totaltime_taxi' as alternative-specific variables
#         df['invehicletime_auto'] = df['totaltime_auto']
#         df['invehicletime_taxi'] = df['totaltime_taxi']

#         # Map the target variable (choice) to its corresponding mode
#         df_y = df['choice'].map({1: 'auto', 2: 'taxi', 3: 'bus', 4: 'subway', 5: 'integmode'})

#         # Reshape the data from wide to long format for multinomial logit model
#         df = xlogit.utils.wide_to_long(
#             df, 
#             id_col='id', 
#             alt_name='alt', 
#             sep='_',
#             alt_list=['auto', 'taxi', 'bus', 'subway', 'integmode'], 
#             empty_val=0,
#             varying=['dist', 'totaltime', 'invehicletime', 'outvehicletime', 'totalcost', 'trans']
#         )

#         # Map the 'choice' column again to the transportation modes
#         df['choice'] = df['choice'].map({1: 'auto', 2: 'taxi', 3: 'bus', 4: 'subway', 5: 'integmode'})

#         # Define Alternative-Specific Constants (ASC) for each transportation mode (auto is used as reference)
#         df['asc_taxi'] = np.ones(len(df)) * (df['alt'] == 'taxi')
#         df['asc_bus'] = np.ones(len(df)) * (df['alt'] == 'bus')
#         df['asc_subway'] = np.ones(len(df)) * (df['alt'] == 'subway')
#         df['asc_integmode'] = np.ones(len(df)) * (df['alt'] == 'integmode')

#         # Convert distance to kilometers (assuming input is in meters)
#         df['dist'] = df['dist'] / 1000  # Unit: km

#         # Convert total cost to 1000 KRW
#         df['totalcost'] = df['totalcost'] / 1000  # Unit: 1000KRW

#         # Station variable is only relevant for subway and integrated modes
#         df['station'] = df['station'] * ((df['alt'] == 'subway') | (df['alt'] == 'integmode'))

#         ### Alternative-Specific Variables (ASVs) ###
#         # Total travel time for each mode
#         df['totaltime_auto'] = df['totaltime'] * (df['alt'] == 'auto')
#         df['totaltime_taxi'] = df['totaltime'] * (df['alt'] == 'taxi')
#         df['totaltime_bus'] = df['totaltime'] * (df['alt'] == 'bus')
#         df['totaltime_subway'] = df['totaltime'] * (df['alt'] == 'subway')
#         df['totaltime_integmode'] = df['totaltime'] * (df['alt'] == 'integmode')

#         # In-vehicle time for each mode
#         df['invehicletime_auto'] = df['invehicletime'] * (df['alt'] == 'auto')
#         df['invehicletime_taxi'] = df['invehicletime'] * (df['alt'] == 'taxi')
#         df['invehicletime_bus'] = df['invehicletime'] * (df['alt'] == 'bus')
#         df['invehicletime_subway'] = df['invehicletime'] * (df['alt'] == 'subway')
#         df['invehicletime_integmode'] = df['invehicletime'] * (df['alt'] == 'integmode')

#         # Out-vehicle time for specific modes (bus, subway, and integrated mode)
#         df['outvehicletime_bus'] = df['outvehicletime'] * (df['alt'] == 'bus')
#         df['outvehicletime_subway'] = df['outvehicletime'] * (df['alt'] == 'subway')
#         df['outvehicletime_integmode'] = df['outvehicletime'] * (df['alt'] == 'integmode')

#         # Define the list of explanatory variables for the model
#         varnames = [
#             'station', 'admin', 'trans', 
#             'asc_taxi', 'asc_bus', 'asc_subway', 'asc_integmode', 
#             'totalcost',
#             'invehicletime_auto', 'invehicletime_taxi', 'invehicletime_bus', 'invehicletime_subway', 'invehicletime_integmode',
#             'outvehicletime_bus', 'outvehicletime_subway', 'outvehicletime_integmode'
#         ]

#         # Initialize the Multinomial Logit model
#         model = xlogit.MultinomialLogit()

#         # Fit the model using the specified variables and data
#         model.fit(X = df[varnames],
#                 y = df['choice'],
#                 varnames = varnames,
#                 isvars = ['admin'],
#                 alts = df['alt'],
#                 ids = df['id']
#         )

#         # Print the model summary to review
#         print(model.summary())
        
#         value_of_invehicletime_auto = (model.coeff_[model.coeff_names == 'invehicletime_auto'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_invehicletime_taxi = (model.coeff_[model.coeff_names == 'invehicletime_taxi'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_invehicletime_bus = (model.coeff_[model.coeff_names == 'invehicletime_bus'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_invehicletime_subway = (model.coeff_[model.coeff_names == 'invehicletime_subway'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_invehicletime_integmode = (model.coeff_[model.coeff_names == 'invehicletime_integmode'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])

#         value_of_outvehicletime_bus = (model.coeff_[model.coeff_names == 'outvehicletime_bus'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_outvehicletime_subway = (model.coeff_[model.coeff_names == 'outvehicletime_subway'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])
#         value_of_outvehicletime_integmode = (model.coeff_[model.coeff_names == 'outvehicletime_integmode'] * 60000) / (model.coeff_[model.coeff_names == 'totalcost'])

#         print('\n----- Result of Value of Travel Time -----')
#         print('승용차 이용자의 통행시간가치 (원/시):', *value_of_invehicletime_auto.astype(int))
#         print('택시 이용자의 통행시간가치 (원/시):', *value_of_invehicletime_taxi.astype(int))
#         print('버스 이용자의 차내 통행시간가치 (원/시):', *value_of_invehicletime_bus.astype(int))
#         print('지하철 이용자의 차내 통행시간가치 (원/시):', *value_of_invehicletime_subway.astype(int))
#         print('버스와 지하철 이용자의 차내 통행시간가치 (원/시):', *value_of_invehicletime_integmode.astype(int))

#         print('버스 이용자의 차외 통행시간가치 (원/시):', *value_of_outvehicletime_bus.astype(int))
#         print('지하철 이용자의 차외 통행시간가치 (원/시):', *value_of_outvehicletime_subway.astype(int))
#         print('버스와 지하철 이용자의 차외 통행시간가치 (원/시):', *value_of_outvehicletime_integmode.astype(int))

#         print('버스의 차내 시간 대비 차외시간의 통행시간가치 비율:', *value_of_outvehicletime_bus / value_of_invehicletime_bus)
#         print('지하철의 차내 시간 대비 차외시간의 통행시간가치 비율:', *value_of_outvehicletime_subway / value_of_invehicletime_subway)
#         print('버스와 지하철의 차내 시간 대비 차외시간의 통행시간가치 비율:', *value_of_outvehicletime_integmode / value_of_invehicletime_integmode)
#         print('------------------\n')

#         # Return the trained model for further use or evaluation
#         return model


#     def predict_MultinomialLogitModel(model, df_X_test, df_y_test):
#         # Concatenate feature data (X) and target data (y) into one DataFrame
#         df = df_X_test

#         # Add an ID column for identifying each individual choice
#         df['id'] = np.arange(len(df))

#         # Rename 'totaltime_auto' and 'totaltime_taxi' as alternative-specific variables
#         df['invehicletime_auto'] = df['totaltime_auto']
#         df['invehicletime_taxi'] = df['totaltime_taxi']

#         # Reshape the data from wide to long format for multinomial logit model
#         df = xlogit.utils.wide_to_long(
#             df, 
#             id_col='id', 
#             alt_name='alt', 
#             sep='_',
#             alt_list=['auto', 'taxi', 'bus', 'subway', 'integmode'], 
#             empty_val=0,
#             varying=['dist', 'totaltime', 'invehicletime', 'outvehicletime', 'totalcost', 'trans']
#         )

#         # Map the 'choice' column again to the transportation modes
#         df['choice'] = df['choice'].map({1: 'auto', 2: 'taxi', 3: 'bus', 4: 'subway', 5: 'integmode'})

#         # Define Alternative-Specific Constants (ASC) for each transportation mode (auto is used as reference)
#         df['asc_taxi'] = np.ones(len(df)) * (df['alt'] == 'taxi')
#         df['asc_bus'] = np.ones(len(df)) * (df['alt'] == 'bus')
#         df['asc_subway'] = np.ones(len(df)) * (df['alt'] == 'subway')
#         df['asc_integmode'] = np.ones(len(df)) * (df['alt'] == 'integmode')

#         # Convert distance to kilometers (assuming input is in meters)
#         df['dist'] = df['dist'] / 1000  # Unit: km

#         # Convert total cost to 1000 KRW
#         df['totalcost'] = df['totalcost'] / 1000  # Unit: 1000KRW

#         # Station variable is only relevant for subway and integrated modes
#         df['station'] = df['station'] * ((df['alt'] == 'subway') | (df['alt'] == 'integmode'))

#         ### Alternative-Specific Variables (ASVs) ###
#         # Total travel time for each mode
#         df['totaltime_auto'] = df['totaltime'] * (df['alt'] == 'auto')
#         df['totaltime_taxi'] = df['totaltime'] * (df['alt'] == 'taxi')
#         df['totaltime_bus'] = df['totaltime'] * (df['alt'] == 'bus')
#         df['totaltime_subway'] = df['totaltime'] * (df['alt'] == 'subway')
#         df['totaltime_integmode'] = df['totaltime'] * (df['alt'] == 'integmode')

#         # In-vehicle time for each mode
#         df['invehicletime_auto'] = df['invehicletime'] * (df['alt'] == 'auto')
#         df['invehicletime_taxi'] = df['invehicletime'] * (df['alt'] == 'taxi')
#         df['invehicletime_bus'] = df['invehicletime'] * (df['alt'] == 'bus')
#         df['invehicletime_subway'] = df['invehicletime'] * (df['alt'] == 'subway')
#         df['invehicletime_integmode'] = df['invehicletime'] * (df['alt'] == 'integmode')

#         # Out-vehicle time for specific modes (bus, subway, and integrated mode)
#         df['outvehicletime_bus'] = df['outvehicletime'] * (df['alt'] == 'bus')
#         df['outvehicletime_subway'] = df['outvehicletime'] * (df['alt'] == 'subway')
#         df['outvehicletime_integmode'] = df['outvehicletime'] * (df['alt'] == 'integmode')

#         # Define the list of explanatory variables for the model
#         varnames = [
#             'station', 'admin', 'trans', 
#             'asc_taxi', 'asc_bus', 'asc_subway', 'asc_integmode', 
#             'totalcost',
#             'invehicletime_auto', 'invehicletime_taxi', 'invehicletime_bus', 'invehicletime_subway', 'invehicletime_integmode',
#             'outvehicletime_bus', 'outvehicletime_subway', 'outvehicletime_integmode'
#         ]

#         df_y_pred = model.predict(X = df[varnames],
#                 varnames = varnames,
#                 isvars = ['admin'],
#                 alts = df['alt'],
#                 ids = df['id']
#         )
        
#         accuracy = accuracy_score(df_y_test, df_y_pred)
#         print('\n----- Result of Accuracy -----')
#         print('정확도: {:.5f}'.format(accuracy))
#         print('------------------\n')