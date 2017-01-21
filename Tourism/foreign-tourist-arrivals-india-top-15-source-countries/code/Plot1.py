import pandas as pd
import matplotlib.pyplot as plt

def plot_line_charts(df,path='.'):
	df2 = df.iterrows()
	for i, row in df2:

		print row.name
		row.plot(legend=True,title='Tourist arrival in india from '+str(row.name))
		#plt.show()
		com_path=path+'/'+ row.name
		print com_path
		plt.savefig(com_path)
		plt.disconnect(1)
		plt.clf()

def plot_pie_charts(df,path='.'):
	list_of_columns = df.columns.tolist()
	col2 = ['#a85ccd', '#8bb337',  '#5e6ed9',  '#52bc60',  '#ce51a0',  '#528444',  '#d04357',  '#50b8a1',  '#ce5129',  '#5e9ad5',  '#d68e32',  '#9273b8', '#c2af54', '#bd6682', '#82712d', '#c57555']
	
	for i in list_of_columns:
		df[i].dropna().plot(kind='pie',colors=col2,autopct='%1.0f%%',figsize=[40,40],title='Tourist arrival in '+i,fontsize=18)
		com_path=path+'/'+ i
		plt.savefig(com_path)
		plt.clf()






data = pd.read_csv('../datafile.csv',index_col='Name of Countries ')



plot_line_charts(data,'/home/sotore/mygov_data_visualization/Tourism/foreign-tourist-arrivals-india-top-15-source-countries/plot/line_charts')
plot_pie_charts (data,'/home/sotore/mygov_data_visualization/Tourism/foreign-tourist-arrivals-india-top-15-source-countries/plot/pie_charts')

