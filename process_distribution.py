import json
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "usage: %s distribution_txt" % sys.argv[0]
        sys.exit(1)
    
    f = open(sys.argv[1], "r")
    dist_lines = f.readlines()

    d = {}
    for line in dist_lines:
        if line == "":
            continue
        depth, count = line.split("\t")
        depth = float(depth)
        count = int(count)
        d[depth] = count

    sea_count_sum = 0
    land_count_sum = 0
    depth_counts = {}
    for depth in sorted(d):
        count = d[depth]
        if depth >= -0.0:
            land_count_sum += int(count)
        else:
            sea_count_sum += int(count)

        rounded_depth = round(float(depth)/10.0)
        if rounded_depth == 0.0 and depth < 0.0:
            # the case when - depths get rounded to 0 thus writing a large number into the array
            continue

        if rounded_depth not in depth_counts:
            depth_counts[rounded_depth] = land_count_sum if depth >= -0.0 else sea_count_sum
        else:
            depth_counts[rounded_depth] += int(count)

    with open("depth_counts.js", "w") as f:
        f.write("var land_value_sum = " + str(land_count_sum) + ";\n")
        f.write("var sea_value_sum = " + str(sea_count_sum) + ";\n")
        f.write("var depth_counts = " + json.dumps(depth_counts) + " ;")

