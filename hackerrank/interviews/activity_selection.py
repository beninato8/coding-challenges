#!/usr/bin/env python3

'''
Given a list of event start times and their durations, return the maximum you can attend
if you can only do one at a time.
This code uses a greedy algorithm.

Examples:

Start    : [1,1,2,3,5]
Duration : [1,2,1,2,2]

End      : [2,3,3,5,7]
Output : len([a0,a2,a3,a4]) == 4
'''

def count_activities_greedy(starts, ends):
    activities = sorted(zip(starts, ends), key=lambda x:x[1]) # sort by earliest end
    count = 0 # track how many activities
    earliest_end = -1 # end time of the last selected activity
    for start, end in activities:
        if start >= earliest_end: # if the current activity starts after the last end
            count += 1
            earliest_end = end # last end is updated to current activity end
    return count

def count_activities_dynamic(starts, ends):
    activities = sorted(zip(starts, ends), key=lambda x:x[0]) # sort by earliest start
    counts = [0] * len(activities)
    count = 0
    for i, (start1, end1) in enumerate(activities): 
        for j, (start2, end2) in enumerate(activities):
            if j < i and end2 <= start1 and counts[i] < counts[j]:
                counts[i] = counts[j] # if any activities ending before start1, add the largest set
        counts[i] += 1 # min count is 1 since activities[i] could be alone
    return max(counts)

def count_activities(starts, durations, method='greedy'):
    ends = (s + d for s,d in zip(starts, durations)) # get end times
    if method == 'dynamic':
        return count_activities_dynamic(starts, ends)
    return count_activities_greedy(starts, ends)

if __name__ == '__main__':
    example1 = [[0,1,2,3,3,5,5,6,8,8,12],[6,3,11,2,5,2,4,4,3,4,2],4]
    example2 = [[1,1,2,3,5],[1,2,1,2,2],4]
    example3 = [[1,3,0,5,3,5,6,8,8,2,12],[3,2,6,2,6,4,4,3,4,12,4],4]
    example4 = [[0,0,0,1,1],[1,1,1,2,1],2]
    example5 = [[0,1,3,3,6],[1,1,1,2,1],4]
    examples = [example1]
    for e in examples:
        print(count_activities(e[0], e[1], method='greedy') == e[2])
        break