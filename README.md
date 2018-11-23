# Maximal_Intersecting_Interval_Problem
Use Heap class to solve the maximal intersecting intervals problem. Given a set of of n open intervals, output all distinct sets of clusters that satisﬁes following conditions:
– Exists point x that lies inside each interval from this set – No other interval can be added to the set.
In the ﬁrst row of the input you are given n followed by left and right end points of each interval (i.e. begin and end). For simplicity let’s assume no interval share end points 
Input: 
5 
1 5 
2 6 
3 8 
7 9 
10 12
Output all maximal intersecting clusters. Intervals are numbered from 1 to n (the line number after the ﬁrst line)
Output: 
1 2 3 
3 4 
5
