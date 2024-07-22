# <ins> 0x00. Pagination </ins>

### Mandatory (4)

1. File: 0-simple_helper_function.py - Write a function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

2. File: 1-simple_pagination.py - Copy index_range from the previous task and the following class into your code and Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

3. File: 2-hypermedia_pagination.py - Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.

4. File: 3-hypermedia_del_pagination.py - Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.
