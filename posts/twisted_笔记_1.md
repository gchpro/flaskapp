title: twisted 笔记 1
date: 2016-12-13 16:25:00
summary: 介绍了一个最小接口文件的组成

===


### twisted 笔记 1

twisted是一个一部异步网络库。


概念解释：

异步(asynchronous):

![asynchronous](./img/asynchronous.jpeg)

	
	An asynchronous program dispatches tasks to devices that can take care of themselves, leaving the program free to do somethings else until it receives a signal that the results are finished.
	异步程序将任务分发到各个能独自处理的设备上去, 程序会一直处于空闲状态直到它收到某个任务已经处理完的信号.
	

并行(parallel):

![asynchronous](./img/parallel.jpg)

	Parallel programs distribute their tasks to multiple processors, that actively work on all of them simultaneously.
	并行程序自动将任务分派到多个处理器上,并且所有任务同步执行.
	
并发(concurrency):

![asynchronous](./img/concurrency.jpeg)


	Concurrent programs handle tasks that are all in progress at the same time, but is is only necessary to work briefly and separately on each task, so the work can be interleaved in whatever order the tasks require.
	并发程序同时处理多个任务,只需要独立地,间歇性的处理各个任务,所以工作可以按照任务需要的任意顺序插入.
	
总结:

并行是指多个任务同时都在执行，一般通过多线程、多进程或多台计算机实现。

并发是指至少两个任务都在推进，不一定是并行的，也可以是时间片切分的方式串行。

类似的，异步（async）未必一定是并行的，但一定是并发的。

