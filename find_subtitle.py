import pysrt

def find_subtitle_in_srt(path_to_srt_file, subtitle_slice):
	subs = pysrt.open(path_to_srt_file)

	len(subs)

	i = 0
	while (subtitle_slice.lower() not in subs[i].text.lower()):
		i += 1

	print "Subtitle is in position: " + str(i)
	print subs[i].text
	return i

index_of_subtitle_slice = find_subtitle_in_srt ('subtitles/taxi_driver.srt', "I'll be over there waiting for you")
index_of_subtitle_slice_end = find_subtitle_in_srt ('subtitles/taxi_driver.srt', "have a good time")

subs = pysrt.open('subtitles/taxi_driver.srt')

new_subs = subs.slice(starts_after={'hours': subs[index_of_subtitle_slice].start.hours,
						 'minutes' : subs[index_of_subtitle_slice].start.minutes,
						 'seconds' : subs[index_of_subtitle_slice].start.seconds},
			ends_before={'hours': subs[index_of_subtitle_slice_end].end.hours,
						 'minutes' : subs[index_of_subtitle_slice_end].end.minutes,
						 'seconds' : subs[index_of_subtitle_slice_end].end.seconds})

new_subs.shift(hours=-1 * new_subs[0].start.hours,
			   minutes=-1 * new_subs[0].start.minutes, 
			   seconds=-1 * new_subs[0].start.seconds)

new_subs.save('subtitles/taxi_driver_after.srt')