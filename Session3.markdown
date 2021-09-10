<img src=".//media/image1.jpeg" style="width:1.38333in;height:0.86667in" />

**Session 3**

**Metaheuristics**

> **Academic year 2020/2021**

The aim of this third practice is to provide a solution to the given
problem by using whatever the students need and that was already
explained in class. The students have to generate a detailed report in
which the methodology used and the analyzes are justified. **Both the
code and the detailed report must be submitted before the deadline,
taking into account that this third practice has a duration of 4
sessions**. Once the documents are submitted, the students will have 2
additional sessions to do an oral presentation describing their
methodology.

The algorithm needs to deal with a database (BD.txt) where each record
(rows in the database) has the following form:

*B 0:A 1:B 2:C 3:D 3:C 4:C 7:E 8:E 10*

This indicates that there is an event B that occurs at time 0; an event
A, which occurs at time 1, etc. Two events can occur at the same instant
of time. For example, event C occurs for the first time at time 3 and
event D also occurs at that instant of time.

The objective is to extract graphs with temporal restrictions so that
the number of records (rows of the database) that this graph fulfills is
the maximum possible. As an example, consider the following database:

> *A 1:B 3:A 4:C 5:C 6:D 7*
>
> *B 2:D 4:A 5:C 7*
>
> *A 1:B 4:C 5:B 6:C 8:D 9*
>
> *B 4:A 6:E 8:C 9*
>
> *B 1:A 3:C 4*
>
> *C 4:B 5:A 6:C 7:D 10*
>
> *A 1:B 2:C 3:C 4:B 5:D 9*

The following graph satisfies three records of the database:

<img src=".//media/image3.jpeg" style="width:2.73889in;height:1.39444in" />

<u>Graph explanation:</u> the event A occurs before B between -1 and 3
gaps of time. That is, B could occur at time 4 and A at time 5 and would
meet the restriction \[-1, 3\]. The event A could also occur at time 2
and B at time 5 and would also meet the restriction \[-1, 3\].

Hence, **the previous graph satisfies the records 1, 3 y 6**:

-   Record 1: it satisfies the graph. The event A occurs at time 1 and B
    > at time 3. The event C occurs at time 5 and fulfills the
    > restriction regarding A and B. The event C also occurs at time 6
    > and fulfills the restriction regarding C, which occurred at
    > time 5. Finally, the event D occurs at time 7 and fulfills the
    > restriction with respect to B.

> <u>There is at least a subset of this record that satisfies the graph.
> In this record there are</u>
>
> <u>two subsets that fulfill the graph, but one is enough</u>:
>
> *A 1:B 3:C 5:C 6:D 7*
>
> *B 3:A 4:C 5:C 6:D 7*

-   Record 2: It only has one C, so it is impossible for it to fulfill
    > the graph.

-   Record 3: The graph fulfills the subset A 1: B 4: C 5: C 8: D 9

-   Record 4: It only has a C and no D, so it is impossible to fulfill
    > the graph.

-   Record 5: It only has a C and it has no D, so it is impossible for
    > it to fulfill the graph.

-   Record 6: The graph fulfills the complete record C 4: B 5: A 6: C 7:
    > D 10

-   Record 7: It does not meet the graph since B 2 and D 9 have a
    > distance of 7 (it does not meet the restriction of the graph). B5
    > and D9 do meet the time restriction of the graph, but, however, B
    > 5 does not meet the restriction with respect to A 1, that is, B 5
    > could not be reached with that graph.

**Important considerations:**

-   Graphs should be as big as possible. A graph considering just two
    > events, e.g. A and B, would be satisfied by a large number of data
    > records, but it would not make sense. Thus, it is established that
    > a graph must have at least 4 events.

-   The graph constraints are important to satisfy the data. Infinite
    > values in a constraint would result in all records being
    > satisfied. Thus, one graph is better than another if the
    > restrictions obtained are as small as possible (ranges).

-   If two graphs satisfy the same records, then the graph with the
    > lowest mean restrictions will be better. That is, whose ranges are
    > lower.

**What to do:**

Obtain a solution to the given problem and considering the provided
database. There is no restriction on the individual encoding, operators,
etc. The only restriction is the exclusive use of the Python language.
The best results obtained by the students during the 4 weeks that the
practices last will be made public, taking into account:

1.  Best solution (number of records satisfied by the graph).

2.  Number of events included in the solution. Minimum 4 events.

3.  Restrictions (small ranges).

4.  Runtime.
