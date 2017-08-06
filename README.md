# Nearmap.com Technical Test
Welcome to the [Nearmap.com](nearmap.com) Python technical test. The purpose of this assignment is to test your familiarity with distributed systems concepts, performance benchmarking and TDD.

## Background
The source code that you are given is a very simple imitation of a name/value store. `DBStore` is the canonical data store that takes a while (50 ms) to store and retrieve data. `CacheStore` is a distributed cache that takes much less time to turn around - 5 ms. This scenario is a simplified example of a typical high performance server cluster with a database, a distributed cache and multiple worker nodes.

## Assumptions
* The solution should start with the DB store and distributed cache empty.
* The application should not assume it is the only instance running in a cluster.
* Provided code can be modified at will.
* The aim of the test is to produce the simplest working solution to the problem. As such you are at liberty to use the Python standard library at will.

## Task
* The objective is to create a data retrival mechanism with lowest possible latency.
* The solution should have a better response time than that one of distributed cache for a frequently requested item, i.e. response time should be faster than 5ms.
* The solution should have unit tests for all new functionality.
* If a value does not exist in the database for a particular key then a new value should be created for the key containing the time of the first thread to populate the value. The time should have microsecond precision.
* The solution must have 10 threads each making 50 consecutive requests for a random key in the range (key0-key9). I.e. there would a total of 500 requests.
* The solution must print the Thread ID, requested key name, returned value, and time to complete that request, similar to the following example:
<pre>
    [1] Request 'key1', response 'value1', time: 50.05 ms
    [2] Request 'key2', response 'value2', time: 50.05 ms
</pre>

## Submission instructions
* It should be possible to run the application by simply invoking
```
python main.py
```
* If the solution is incomplete, please state what hasn't been finished and outline how you are planning on solving it.
* DO NOT send pull requests against this repository because we don't want other candidates to see your solution.
