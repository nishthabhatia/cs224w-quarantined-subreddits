import glob, os
import csv

def to_csv(filename):
    # input = open(filename, "r")
    outname = "%s.csv" % os.path.splitext(filename)[0]
    with open(outname, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Subreddit', 'Num Nodes', 'Num Edges',
            'Average Clustering Coefficient', 'Pagerank',
            'Number of Connect Components', 'Average Degree Centrality',
            'Average Neighbor Degree', 'Average Degree',
            'Standard Deviation of Degree'])

        lines = [line.rstrip('\n') for line in open(filename)]

        row = []
        for i, line in enumerate(lines):
            if ':' not in line:
                continue
            start_index = line.index(':') + 2
            if (i % 12 == 0):
                subreddit_name = line[start_index:]
                end_index = subreddit_name.index("Graphs.txt")
                subreddit_name = subreddit_name[0:end_index]
                row.append(subreddit_name)
            else:
                row.append(line[start_index:])
            if ((i + 3) % 12 == 0):
                filewriter.writerow(row)
                row = []




if __name__ == "__main__":
    os.chdir(".")
    for file in glob.glob("*.txt"):
        print(file)
        to_csv(file)
