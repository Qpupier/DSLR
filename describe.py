# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    describe.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qpupier <qpupier@student.42lyon.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/24 15:04:40 by qpupier           #+#    #+#              #
#    Updated: 2026/09/24 16:42:22 by qpupier          ###   ########lyon.fr    #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
datas = []
columns = []
for column in df.columns:
	if column != "Hogwarts House" and column != "Index" and pd.api.types.is_numeric_dtype(df[column]):
		columns.append(column)
		datas.append(df[column].sort_values().to_list())
lines = {}
line_count = []
line_mean = []
line_std = []
line_min = []
line_ft_quartile = []
line_median = []
line_th_quartile = []
line_max = []
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
	line_count.append(count)
	line_mean.append(total / count if count > 0 else 0)
	line_min.append(min)
	line_ft_quartile.append(data[int(count * 0.25)] if count > 0 else 0)
	line_median.append(data[int(count * 0.5)] if count > 0 else 0)
	line_th_quartile.append(data[int(count * 0.75)] if count > 0 else 0)
	line_max.append(max)
for data in datas:
	std = 0
	for nb in data:
		if pd.notna(nb):
			std += (nb - line_mean[datas.index(data)]) ** 2
	line_std.append((std / line_count[datas.index(data)]) ** 0.5 if line_count[datas.index(data)] > 0 else 0)
lines["Count"] = line_count
lines["Mean"] = line_mean
lines["Std"] = line_std
lines["Min"] = line_min
lines["25%"] = line_ft_quartile
lines["50%"] = line_median
lines["75%"] = line_th_quartile
lines["Max"] = line_max
result = pd.DataFrame.from_dict(lines, orient="index", columns=columns)
print(result)
