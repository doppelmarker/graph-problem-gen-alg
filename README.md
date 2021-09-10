<img src=".//media/image1.jpeg" style="width:1.38333in;height:0.86667in" />

\*\*Session 3\*\*

\*\*Metaheuristics\*\*

\> \*\*Academic year 2020/2021\*\*

The aim of this third practice is to provide a solution to the given

problem by using whatever the students need and that was already

explained in class. The students have to generate a detailed report in

which the methodology used and the analyzes are justified. \*\*Both the

code and the detailed report must be submitted before the deadline,

taking into account that this third practice has a duration of 4

sessions\*\*. Once the documents are submitted, the students will have 2

additional sessions to do an oral presentation describing their

methodology.

The algorithm needs to deal with a database (BD.txt) where each record

(rows in the database) has the following form:

* B 0:A 1:B 2:C 3:D 3:C 4:C 7:E 8:E 10\*

This indicates that there is an event B that occurs at time 0; an event

A, which occurs at time 1, etc. Two events can occur at the same instant

of time. For example, event C occurs for the first time at time 3 and

event D also occurs at that instant of time.

The objective is to extract graphs with temporal restrictions so that

the number of records (rows of the database) that this graph fulfills is

the maximum possible. As an example, consider the following database:

\> \*A 1:B 3:A 4:C 5:C 6:D 7\*

\>

\> \*B 2:D 4:A 5:C 7\*

\>

\> \*A 1:B 4:C 5:B 6:C 8:D 9\*

\>

\> \*B 4:A 6:E 8:C 9\*

\>

\> \*B 1:A 3:C 4\*

\>

\> \*C 4:B 5:A 6:C 7:D 10\*

\>

\> \*A 1:B 2:C 3:C 4:B 5:D 9\*

The following graph satisfies three records of the database:

<img src=".//media/image2.jpeg" style="width:2.73889in;height:1.39444in" />

<u>Graph explanation:</u> the event A occurs before B between -1 and 3

gaps of time. That is, B could occur at time 4 and A at time 5 and would

meet the restriction \[-1, 3\]. The event A could also occur at time 2

and B at time 5 and would also meet the restriction \[-1, 3\].

Hence, \*\*the previous graph satisfies the records 1, 3 y 6\*\*:

- Record 1: it satisfies the graph. The event A occurs at time 1 and B

\> at time 3. The event C occurs at time 5 and fulfills the

\> restriction regarding A and B. The event C also occurs at time 6

\> and fulfills the restriction regarding C, which occurred at

\> time 5. Finally, the event D occurs at time 7 and fulfills the

\> restriction with respect to B.

\> <u>There is at least a subset of this record that satisfies the graph.

\> In this record there are</u>

\>

\> <u>two subsets that fulfill the graph, but one is enough</u>:

\>

\> \*A 1:B 3:C 5:C 6:D 7\*

\>

\> \*B 3:A 4:C 5:C 6:D 7\*

- Record 2: It only has one C, so it is impossible for it to fulfill

\> the graph.

- Record 3: The graph fulfills the subset A 1: B 4: C 5: C 8: D 9

- Record 4: It only has a C and no D, so it is impossible to fulfill

\> the graph.

- Record 5: It only has a C and it has no D, so it is impossible for

\> it to fulfill the graph.

- Record 6: The graph fulfills the complete record C 4: B 5: A 6: C 7:

\> D 10

- Record 7: It does not meet the graph since B 2 and D 9 have a

\> distance of 7 (it does not meet the restriction of the graph). B5

\> and D9 do meet the time restriction of the graph, but, however, B

\> 5 does not meet the restriction with respect to A 1, that is, B 5

\> could not be reached with that graph.

\*\*Important considerations:\*\*

- Graphs should be as big as possible. A graph considering just two

\> events, e.g. A and B, would be satisfied by a large number of data

\> records, but it would not make sense. Thus, it is established that

\> a graph must have at least 4 events.

- The graph constraints are important to satisfy the data. Infinite

\> values in a constraint would result in all records being

\> satisfied. Thus, one graph is better than another if the

\> restrictions obtained are as small as possible (ranges).

- If two graphs satisfy the same records, then the graph with the

\> lowest mean restrictions will be better. That is, whose ranges are

\> lower.

\*\*What to do:\*\*

Obtain a solution to the given problem and considering the provided

database. There is no restriction on the individual encoding, operators,

etc. The only restriction is the exclusive use of the Python language.

The best results obtained by the students during the 4 weeks that the

practices last will be made public, taking into account:

1. Best solution (number of records satisfied by the graph).

1. Number of events included in the solution. Minimum 4 events.

1. Restrictions (small ranges).

1. Runtime.

Graph problem. Genetic algorithm
# Contents
[**Encoding** 1](#encoding)

[**Initial generation creation** 2](#initial-generation-creation)

[**Restrictions of transitions** 2](#restrictions-of-transitions)

[**Crossover and mutation operators**
5](#crossover-and-mutation-operators)

[**Crossover** 5](#crossover)

[**Mutation** 6](#mutation)

[**Evaluation** 7](#evaluation)

[**Notes and observations** 13](#notes-and-observations)

[**Interesting solutions obtained** 15](#interesting-solutions-obtained)
# **<u>Encoding</u>**
The most important thing – **encoding**.

The way to encode our solutions is the following:

<img src=".//media/image1.png" style="width:6.725in;height:0.175in" />

This is a list of lists, each of inner lists implies a single transition
between 2 events in the graph. The first value of the transition is our
starting point, the second value is the end point, the third and the
fourth values mean our restriction limit.

*Whenever a graph contains similar events, e.g. C is met 3 times, then
duplicates are encoded with tilde: C, C’, C’’ and so on.*
# **<u>Initial generation creation</u>**
Step 1: we create a list of random events within the given number:

<img src=".//media/image2.png" style="width:2.975in;height:0.225in" />

Step 2: we create a graph (dictionary):

<img src=".//media/image3.png" style="width:3.4in;height:0.225in" />

Step 3:

<img src=".//media/image4.png" style="width:2.825in;height:3.43398in" />

We need to avoid incorrect graphs:

<img src=".//media/image5.png" style="width:3.01667in;height:0.43333in" />

Checking this condition lets us avoid them:

if vertex not in all\_values and len(graph\[vertex\]) == 0:

By this moment, we have obtained a correct graph. Now we need to adjust
it to our final encoding by adding restrictions.
## **<u>Restrictions of transitions</u>**
The idea to find the **restrictions** for transitions between events in
the graph is the following:

• ***Find pivots***: run through all the records in the database and
evaluate average values of all events (we totally have 5 events: A, B,
C, D, E).

• Round them to the closest integer. At this stage we have obtained
these pivots: A – 9, B – 8, C – 12, D – 13, E – 20.

The fact, that we have obtained these pivots means that values in the DB
are distributed vastly in the left part of this limit: \[0…40\].

• Now it’s time to define the ***restriction deviation***. Restriction
deviation is a number which indicates the biggest possible deviation
from the pivots. For example, we have defined a restriction deviation
equal to 5. Let’s assume we have a transition from A to B in our graph.
A and B pivots are 9 and 8 respectively. 8 - 9 = -1. -1 is the value
which now can be varied by restriction deviation. So, the ***<u>lowest
value</u> of our limit*** is obtained by ***<u>subtraction</u> of a
random number from 0 to 5*** and the ***<u>highest value</u> of our
limit*** is obtained by ***<u>addition</u> of a random number again from
0 to 5***.

• So, every time with a new transition in the graph we evaluate its
difference and apply deviation. By this moment we have obtained the
restrictions for all of our transitions.

Step 4:

<img src=".//media/image6.png" style="width:6.11002in;height:2.36667in" />

Now we want to introduce the test which shows the dependency between the
<u>restrictions deviation</u> and <u>generation evaluation runtime</u>.

Number of ***elitism function launch <u>repetitions</u>*** used – 5.

***Number of generations*** – 5.

***Graphs in generation*** – 10.

***Events per graph*** – 4.

|**Restrictions deviation**|**Average evaluation runtimes, sec**|
| :-: | :-: |
|5|2,04|
|4|1,27|
|3|0,87|
|2|0,71|
|1|0,52|

***So, it’s not difficult to notice that whenever the restrictions
deviation is higher, the average evaluation runtimes are also higher***.
The cause of this behavior lies in the implementation of evaluation
function and seems to be transparent: higher restrictions deviation
changes graphs’ restrictions more significantly and such graphs more
likely become incompatible with restrictions in the rows of a database,
thus they are filtered out from evaluation process very quickly, which
reduces the runtime.
# **<u>Crossover and mutation operators</u>**
In this assignment a decision was made to apply a genetic algorithm with
elitism approach, so, the best solutions (1/2 of generation size) are
transmitted into the next generation, other solutions are obtained by
performing crossover and mutation operators.
## **<u>Crossover</u>**
***Crossover operator*** works like this:

<img src=".//media/image7.png" style="width:3.89167in;height:2.15in" />

So, basically, we split our solution in the middle and share the
***restrictions***, not the transitions, because we can easily ruin the
correctness of the graph in this case. But there is a tricky moment: due
to the fact that our solution’s size may vary (different graphs may have
different amount of transitions between the events), a crossover move
may be performed not completely like on the picture above. The second
solution obtains -9 and -6 restrictions from the first one, but 3,7 are
not transmitted, because there is not enough space for them. **Well, we
believe, it’s very hard to find out a definitely good crossover operator
and adjust it to this problem, because in our case the
*<u>restrictions</u>* *<u>are generated precisely to an exact
transition</u>*, and sharing the restrictions among different
transitions may move us away from a better solution, so it has been
decided to <u>set a crossover probability</u> to a comparatively low
value – <u>around 0,5</u>** **or even lower.**
## **<u>Mutation</u>**
Concerning ***mutation operator***, the idea is to take a random gene
(transition between 2 events) and expand its restrictions by 1 (subtract
1 from the lowest point and add 1 to the highest point). We are ***only
expanding restrictions***, because this will let us increase the fitness
values of our solutions, we are ***not interested in constricting*** our
restrictions more, ***because we are able to tune its value by
restrictions deviation***. ***Mutation probability*** is set somewhere
***<u>around 0,6</u>*** by this moment.
# **<u>Evaluation</u>**
***Fitness value** is purely represented by the **number of records**
satisfied by the graph.*

Step 1: transform original graph into a dictionary without limits:

<img src=".//media/image8.png" style="width:5.625in;height:0.23333in" />

Step 2: transform record in DB into a dictionary:

<img src=".//media/image9.png" style="width:5.33333in;height:0.225in" />

Step 3: obtain **<u>total\_travel\_list</u>**:

<img src=".//media/image10.png" style="width:6.725in;height:0.18333in" />

<img src=".//media/image11.png" style="width:6.725in;height:0.175in" />

Step 4: clear out transitions from total travel list which don’t obey
necessary limits:

<img src=".//media/image12.png" style="width:6.725in;height:0.19167in" />

Whenever a list which corresponds to transition in our graph is empty,
then we can conclude that we can not perform this transition, and that’s
why this record can’t be satisfied by the graph (function returns False,
like in our case).

It’s necessary to denote that a bigger number of events (bigger number
of transitions as a result) and wider restrictions limits provide us
with a bigger **<u>total\_travel\_list</u>** which leads to higher
runtimes.

Step 5: if we have succeeded by this moment, then we may have this total
travel list:

<img src=".//media/image13.png" style="width:6.71667in;height:0.80833in" />

We create all the possible routes of these transitions:

<img src=".//media/image14.png" style="width:6.725in;height:2.69167in" />

Step 6: big loop starts. We take each of the routes and build a
corresponding graph which would satisfy this route:

<img src=".//media/image15.png" style="width:4.83333in;height:0.20833in" />

<img src=".//media/image16.png" style="width:4.11667in;height:0.19167in" />

Step 7: we change the values of events in our graph\_remade to hatches
depending on the occurrence order:

<img src=".//media/image17.png" style="width:3.86667in;height:0.25in" />

Step 8: we compare this obtained graph with the original one:

<img src=".//media/image18.png" style="width:4.65833in;height:0.21667in" />

<img src=".//media/image17.png" style="width:3.86667in;height:0.25in" />

Whenever these graphs are equal, then we have found at least one correct
route, the process of routes traversing is now terminated and we make a
conclusion that this record in the DB is satisfied by the given graph
(function returns True).

If there are no correct routes, then the record in the DB is not
satisfied by the given graph (function returns False).
# **<u>Fitness value distribution graphs</u>**
c\_prob = 0.5
m\_prob = 0.6

graphs\_amount = 10
graphs\_size = 4
restrictions\_deviation = 5
num\_generations = adjusted

<img src=".//media/image19.png" style="width:4in;height:3in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_3.png" />

<img src=".//media/image20.png" style="width:4in;height:3in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_6.png" />

<img src=".//media/image21.png" style="width:3.75in;height:2.8125in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_1.png" />

<img src=".//media/image22.png" style="width:3.77778in;height:2.83333in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_01.png" />

c\_prob = 0.5
m\_prob = 0.6

graphs\_amount = 10
graphs\_size = 4
restrictions\_deviation = 3
num\_generations = adjusted

<img src=".//media/image23.png" style="width:3.79167in;height:2.84375in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_21.png" />

<img src=".//media/image24.png" style="width:3.82222in;height:2.86667in" alt="C:\Users\ghost\Figure\_221.png" />

<img src=".//media/image25.png" style="width:3.67778in;height:2.75833in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_2221.png" />

c\_prob = 0.5
m\_prob = 0.6

graphs\_amount = 10
graphs\_size = 5
restrictions\_deviation = 3
num\_generations = adjusted

<img src=".//media/image26.png" style="width:3.83333in;height:2.875in" alt="C:\Users\ghost\OneDrive\Desktop\Figure\_2111.png" />
# **<u>Notes and observations</u>**
- The database was generated by some kind of an algorithm, that’s why
  many records have a very close pattern:

<img src=".//media/image27.png" style="width:6.325in;height:2.89167in" />

This means we could actually find a better way to find pivots for
restrictions creation.

- Regarding the number of events per graph:

Number of ***elitism function launch <u>repetitions</u>*** used – 5.

***Number of generations*** – 5.

***Graphs in generation*** – 10.

***Restrictions deviation*** – adjusted.

|**Events per graph**|**Average evaluation runtimes, sec**|**Restrictions deviation**|
| :-: | :-: | :-: |
|4|2,04|5|
|5|7,3|5|
|6|2,36|3|
|7|1,31|2|

So, the problem of our algorithm is that the evaluation time rises
significantly when the number of events is increased (number of
transitions). That’s why we can perform the algorithm with big events
amount only with less restrictions deviation, because it filters out
incompatible solutions quickly.
# **<u>Interesting solutions obtained</u>**
***Our favorite solutions are marked with green color.***

c\_prob = 0.5
m\_prob = 0.6

graphs\_amount = 10
graphs\_size = 4
restrictions\_deviation = adjusted
num\_generations = 5

\['B', 'A', -1, 3\], \['B', 'C', 2, 6\], \['A', 'C', 2, 3\], \['C', 'D',
-1, 3\] Fitness – 583.

\[\['C', 'D', -3, 3\], \['D', "C'", -6, 2\], \["C'", 'C', -5, 2\],
\["C'", 'A', -8, -2\]\] Fitness – 589.

\[\['C', "C'", -1, 2\], \['C', 'D', -1, 1\], \["C'", 'A', -8, 0\],
\['A', 'C', 3, 6\], \['D', 'A', -8, -1\]\] Fitness – 589.

\[\['C', "C'", -2, 0\], \["C'", 'D', -3, 4\], \["C'", "C''", -3, 0\],
\["C''", 'D', -1, 3\], \["C''", 'C', 0, 4\]\] Fitness – 589. (Best)

*It can be noticed that this solution contains almost only C events.*

The number of events occurrences in the DB:

A – 1256, B – 1587, C – 3064, D – 1056, E – 1608.

\[\['A', 'C', 2, 5\], \['A', 'D', -1, 3\], \['C', 'E', 4, 9\], \['E',
'A', -12, -9\], \['D', 'C', -2, 2\]\] Fitness – 525.

\[\['B', 'D', 0, 6\], \['A', 'D', -1, 4\], \['A', 'C', 1, 6\]\] Fitness
– 589.

c\_prob = 0.5
m\_prob = 0.6

graphs\_amount = 10
graphs\_size = 5
restrictions\_deviation = adjusted
num\_generations = 5

\[\['C', 'B', -4, 0\], \['C', "C'", -2, 0\], \['C', 'D', -2, 3\], \['A',
'C', 2, 3\], \['A', "C'", 0, 4\], \['B', 'D', 2, 5\], \["C'", 'D', -1,
4\], \['D', 'A', -7, -2\]\] Fitness – 110.

\[\['B', 'E', 10, 14\], \['B', 'C', 4, 8\], \['E', "B'", -15, -8\],
\['E', 'C', -8, -7\], \["B'", 'C', 1, 5\], \['C', 'A', -3, 1\], \['A',
'E', 9, 15\]\] Fitness – 122.

\[\['B', "B'", -2, 8\], \["B'", 'C', 2, 4\], \['C', 'D', -4, -1\],
\['E', 'B', -15, -10\], \['E', 'C', -9, -6\], \['D', 'E', 7, 11\]\]
Fitness – 218.

\[\['C', "C'", -4, 0\], \['B', "C'", 1, 3\], \['D', 'C', -1, 3\], \['D',
"C'", -2, 2\], \['A', "C'", 2, 5\], \['A', 'B', -1, 0\]\] Fitness – 124.

\[\['C', 'D', -2, 1\], \['C', "C'", -3, 2\], \['C', 'B', -4, 0\], \['D',
'A', -7, -2\], \["C'", 'B', -8, -1\], \['A', 'C', 0, 5\], \['B', 'A', 1,
3\]\] Fitness – 123.

\[\['A', 'C', 2, 6\], \['C', 'E', 5, 9\], \['B', 'E', 11, 16\], \['B',
'A', -2, 1\], \['B', 'C', 2, 8\], \["B'", 'A', -2, 1\]\] Fitness – 123.

\[\['A', 'C', 3, 6\], \['C', 'B', -8, -3\], \['B', 'A', -1, 4\], \['E',
'C', -9, -5\], \["C'", 'B', -8, -2\]\] Fitness – 208.

Well, we have obtained graphs which contain 6 events and satisfy some
amount of records in the database (close to 0), but unfortunately they
were not saved, so we can not introduce them here.

We have not discovered graphs with 7 events which satisfy at least 1 row
in the database, but it doesn’t mean that there are no such graphs.
