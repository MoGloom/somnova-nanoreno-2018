init offset = -3

# DynamicMusic is a custom class I defined in dynamicmusic.rpy.
# file_names is an array of up to two files which have identical timing (i.e. can be crossfaded between).
# stop_points is a list of points at which the song can be stopped (in seconds).
# loop_point is the point from which a song can be looped (from the beginning).
#
# To use this in a script, use the following command:
# $ queue_music(music_jazz_tune)
#
# To crossfade, use the following command:
# $ crossfade_music(0.0, 1.0, 5.0)
# This sets the first track's volume to 0.0 and the second track's volume to 1.0 over the course
# of five seconds.

define music_one = DynamicMusic(["music/one.ogg", "music/one-reverb.ogg"], stop_points = [0], loop_point = 61.324)

define music_three1 = DynamicMusic(["music/three-1.ogg"], stop_points = [22.978, 43.404, 63.829, 84.255, 109.787, 130.212, 150.638, 176.170, 196.595], loop_point = 22.978)
define music_three2 = DynamicMusic(["music/three-2.ogg"], stop_points = [0], loop_point = 0)

define music_four1 = DynamicMusic(["music/four-1.ogg", "music/four-1-reverb.ogg"], stop_points = [4.174, 8.348, 12.522, 16.696, 20.870, 25.043, 29.217, 33.391, 37.565, 41.739, 45.913, 50.087, 54.261, 58.435, 62.609, 66.783, 70.957, 75.130, 79.304, 83.478, 87.652, 91.826, 96, 100.174, 104.348, 108.522], loop_point = 41.739)
define music_four2 = DynamicMusic(["music/four-2.ogg", "music/four-2-reverb.ogg"], stop_points = [4.174, 8.348, 12.522, 16.696, 20.870, 25.043, 29.217, 33.391, 37.565, 41.739, 45.913, 50.087, 54.261, 58.435, 62.609, 66.783], loop_point = 0)

define music_five = DynamicMusic(["music/five-1.ogg", "music/five-2.ogg"], stop_points = [3.133, 06.467, 9.8, 13.133, 16.467, 19.8, 23.133, 26.467, 29.8, 33.133, 36.467, 39.8, 43.133, 46.667, 49.8, 53.133, 56.467, 59.8, 63.133, 66.467, 66.467, 73.133, 76.467, 79.8, 83.133, 86.467, 89.8, 93.133, 96.467, 99.8, 103.133, 106.467, 109.8, 113.133, 116.467, 119.8, 123.133, 126.467, 129.8, 133.133, 136.467, 139.8, 143.133, 146.667, 149.8, 153.133, 156.467, 159.8, 163.133, 166.467, 169.8, 173.133, 176.467, 179.8, 183.133, 186.467, 189.8, 193.133, 196.467, 199.8, 203.133, 206.467, 209.8, 213.133, 216.467, 219.8], loop_point = 48.333) # "music/five-1-reverb.ogg" and "music/five-2-reverb.ogg" are on standby until crossfade allows for four simultaneous tracks

define music_seven1 = DynamicMusic(["music/seven-1.ogg"], stop_points = [29.189, 38.918, 48.648, 68.108, 126.486, 165.405], loop_point = 29.189)
define music_seven2c = DynamicMusic(["music/seven-2c.ogg"], stop_points = [58.378, 77.837, 97.297], loop_point = 58.738)
define music_seven2r = DynamicMusic(["music/seven-2r.ogg"], stop_points = [0], loop_point = 58.738)
define music_seven3 = DynamicMusic(["music/seven-3.ogg"], stop_points = [0], loop_point = 0)

define music_nine = DynamicMusic(["music/nine-1.ogg"], stop_points = [5.909, 8.636, 11.364, 14.091, 16.818, 19.545, 22.273, 25.0, 27.727, 30.455, 33.182, 35.909, 38.636, 41.364, 44.091, 46.818, 49.545, 52.273, 55.0, 57.727, 60.455, 63.182, 65.909, 68.636, 71.364, 74.091, 76.818, 79.545, 82.273, 85.0, 87.727, 90.455, 93.182, 95.909, 98.636, 101.364, 104.091, 106.818, 109.545, 112.273, 115.0, 117.727, 120.455, 123.182, 125.909, 128.636, 131.364, 134.091, 136.818, 139.545, 142.273, 145.0, 147.727, 150.455, 153.182, 155.909, 158.636, 161.364, 164.091, 166.818, 169.545, 172.273, 175.0, 177.727, 180.455, 183.182, 185.909, 188.636, 191.364, 194.091, 196.818, 199.545, 202.273, 205.0, 207.727, 210.455, 213.182, 215.909, 218.636, 221.364], loop_point = 5)
define music_nine2 = DynamicMusic(["music/nine-2.ogg"], stop_points = [0], loop_point = 0)

define music_test = DynamicMusic(["music/test1.ogg", "music/test2.ogg"], stop_points = [0], loop_point = 0)

define placeholder = DynamicMusic(["music/placeholder.ogg", "music/test2.ogg"], stop_points = [0], loop_point = 0)