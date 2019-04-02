import csv


csv_file = open('data.csv', 'w')
reader = csv.writer(csv_file)
csv_writer = csv.writer(csv_file)
# for hn_link
csv_writer.writerow(['headline', 'summary', 'video_link'])	
			

