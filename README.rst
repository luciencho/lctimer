LucienTimer
=========

A package for timer the duplicated python codes.

Installation
============

.. code-block:: bash

    $ pip install lctimer

Usage
=====

.. code-block:: python

    from lctimer import timer

    @timer.record
    def foo():
    	a = 0
    	for _ in range(100000):
    		a += 1


    @timer.record
    class B:

    	def __init__(self):
    		self.words = 'testing'

    	@staticmethod
    	def ioo():
    		c = 0
    		for _ in range(100000):
    			c += 1
    	c = 0


    if __name__ == '__main__':
    	for _ in range(5):
    		foo()
    		B.ioo()

    	timer.sum_up()
    	# Function: "ioo"	Best: 4.01 ms	Average: 4.81 ms	Worst: 5.04 ms	Total Loops: 5
    	# Function: "foo"	Best: 4.01 ms	Average: 4.42 ms	Worst: 5.04 ms	Total Loops: 5