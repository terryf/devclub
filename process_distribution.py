import json

f = open("distribution.bedrock.altitude.txt", "r")
dist_lines = f.readlines()

d = {}
for line in dist_lines:
    if line == "":
        continue
    depth, count = line.split("\t")
    depth = float(depth)
    count = int(count)
    d[depth] = count

count_sum = 0
depth_counts = {}
for depth in sorted(d):
    count = d[depth]
    count_sum += int(count)
    rounded_depth = round(float(depth)/10.0)
    if rounded_depth not in depth_counts:
        depth_counts[rounded_depth] = count_sum
    else:
        depth_counts[rounded_depth] += int(count)

with open("depth_counts.js", "w") as f:
    f.write("var value_sum = " + str(count_sum) + ";\n")
    f.write("var depth_counts = " + json.dumps(depth_counts) + " ;")
    
