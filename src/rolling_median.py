""" Calculates the median degree of a venmo transaction graph """

import argparse
import collections
import datetime
import heapq
import sys
import os
import json

from utils import graph


def process_transaction(g, ts, actor, target):
	# print ts, actor, target
	ts = datetime.datetime.strptime(ts, '%Y-%m-%dT%H:%M:%SZ')
	if not g.ts_end or ts > g.ts_end:
		g.ts_end = ts
		g.ts_start = g.ts_end - datetime.timedelta(seconds=60)
	# print g.ts_start, g.ts_end

	g.addEdge(actor, target)

	heapq.heappush(g.heap, (ts, [actor, target]))

	while g.heap:
		min_ts, [u, v] = min(g.heap)
		if min_ts < g.ts_start:
			created_time, [u, v] = heapq.heappop(g.heap)
			g.removeEdge(u, v)
		else:
			break


def find_median(g):
	arr = [len(g.adjList[v]) for v in g.adjList]
	arr = sorted(arr)
	half, odd = divmod(len(arr), 2)
	if odd:
		return arr[half]
	return (arr[half - 1] + arr[half]) / 2.0


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('input_file', help='Path to input file')
	parser.add_argument('output_file', help='Path to output file')
	args = parser.parse_args()

	g = graph.Graph()

	with open(args.input_file, 'r') as f:
		lines = f.readlines()
		for line in lines:
			line = json.loads(line)
			process_transaction(g, line['created_time'], line['actor'], line['target'])
			median = find_median(g)
			with open(args.output_file, 'a') as out:
				out.write(str(median)+'\n')

