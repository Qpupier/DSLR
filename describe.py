# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/24 15:04:40 by qpupier           #+#    #+#              #
#    Updated: 2026/09/30 18:12:52 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

from utils import *

if __name__ == "__main__":
	if len(sys.argv) != 2:
		error(f"Usage: python describe.py <dataset.csv>")
	df = parse_csv(sys.argv[1])
	df_size = len(df)
	datas = []
	columns = []
	for column in df.columns:
		if column != COLUMN_INDEX_NAME and column != COLUMN_HOUSE_NAME and pd.api.types.is_numeric_dtype(df[column]):
			columns.append(column)
			datas.append(df[column].sort_values().to_list())
	lines = {}
	line_count = []
	line_mean = []
	line_std = []
	line_min = []
	line_ft_quartile = []
	line_median = []
	line_rd_quartile = []
	line_max = []
	line_skewness = []
	for data in datas:
		count = 0
		total = 0
		min = None
		for nb in data:
			if pd.notna(nb):
				count += 1
				total += nb
				if not min:
					min = nb
				max = nb
		if not count:
			error("The dataset is empty or contains only NaN values.")
		if count % 2:
			median = data[int(count * 0.5)]
		else:
			median = (data[int(count * 0.5) - 1] + data[int(count * 0.5)]) / 2
		if count % 4:
			ft_quartile = data[int(count * 0.25)]
			rd_quartile = data[int(count * 0.75)]
		else:
			ft_quartile = (data[int(count * 0.25) - 1] + data[int(count * 0.25)]) / 2
			rd_quartile = (data[int(count * 0.75) - 1] + data[int(count * 0.75)]) / 2
		line_count.append(count)
		line_mean.append(total / count if count > 0 else 0)
		line_min.append(min)
		line_ft_quartile.append(ft_quartile)
		line_median.append(median)
		line_rd_quartile.append(rd_quartile)
		line_max.append(max)
	for data in datas:
		std = 0
		for nb in data:
			if pd.notna(nb):
				std += (nb - line_mean[datas.index(data)]) ** 2
		line_std.append((std / count) ** 0.5 if count > 0 else 0)
		skewness = 0
		for nb in data:
			if pd.notna(nb):
				skewness += ((nb - line_mean[datas.index(data)]) / line_std[datas.index(data)]) ** 3
		line_skewness.append(skewness / count if count > 0 else 0)
	lines["Count"] = line_count
	lines["Mean"] = line_mean
	lines["Std"] = line_std
	lines["Min"] = line_min
	lines["25%"] = line_ft_quartile
	lines["50%"] = line_median
	lines["75%"] = line_rd_quartile
	lines["Max"] = line_max
	lines["Range"] = [max - min for max, min in zip(line_max, line_min)]
	lines["IQR"] = [rd_quartile - ft_quartile for rd_quartile, ft_quartile in zip(line_rd_quartile, line_ft_quartile)]
	lines["Skewness"] = line_skewness
	lines["Missing"] = [df_size - count for count in line_count]
	lines["Missing (%)"] = [round((df_size - count) / df_size * 100, 2) for count in line_count]
	result = pd.DataFrame.from_dict(lines, orient="index", columns=columns)
	print(result)
