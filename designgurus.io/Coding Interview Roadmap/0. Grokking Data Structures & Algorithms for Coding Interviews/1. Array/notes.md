
# Table of content
- [Table of content](#table-of-content)
- [Introduction to Arrays](#introduction-to-arrays)
  - [Fixed or Dynamic Size Arrays](#fixed-or-dynamic-size-arrays)
  - [Basic Concepts and Operations](#basic-concepts-and-operations)
  - [Những lưu ý về mảng khi tham gia phỏng vấn](#những-lưu-ý-về-mảng-khi-tham-gia-phỏng-vấn)

# <div style="text-align:center">Introduction to Arrays</div>

Array is one of the fundamental data structures and is used extensively in 
software development. Arrays provide a means of storing and organizing data in 
a systematic, computer-memory-efficient manner.

Essentially, an array is a collection of elements, each identified by 
an array index. The array elements are stored in contiguous memory locations, 
meaning they are stored in a sequence.


## Fixed or Dynamic Size Arrays

Arrays can be categorized into two types based on their ability to adjust size:

- Static Arrays: These arrays maintain a fixed size, determined during 
  declaration and unchangeable throughout the program's execution. 
  Memory allocation is performed once, and the array's size never changes.

- Dynamic Arrays: Contrary to static arrays, dynamic arrays can adjust 
  their size during runtime, adapting to the volume of data they store. 
  This adaptability allows efficient memory usage but might also involve 
  additional operations (such as creating a new array and copying elements) 
  when resizing is needed, imposing an overhead on certain operations.

Various programming languages handle arrays differently, which can impact 
the efficiency of array operations. For example, languages like Python, 
JavaScript, Ruby, and PHP use dynamic arrays, where you don't need to specify 
the size in advance when creating an array (or list in Python). 
This makes these languages more user-friendly for coding interviews.

## Basic Concepts and Operations

1. Accessing Elements

    Each element within an array can be accessed using its index, which denotes 
    the position of the element in the array. The indices typically commence 
    from zero, meaning the first element is accessed using array[0], 
    the second with array[1], and so forth. Accessing elements in an array 
    is an $O(1)$ time complexity operation, as it directs to the precise memory 
    location without requiring iteration through other elements.

2. Inserting Elements

    The insertion of elements can be executed in multiple ways, depending upon 
    the requisite application:

    - **At the End**: An element may be inserted at the end of an array, 
    - which is usually an $O(1)$ operation.

    - **At a Specific Index**: If insertion is desired at a particular index, 
    subsequent elements must be shifted to make room, 
    escalating the time complexity to $O(n)$ in the worst case.
1. Deleting Elements
    Deleting elements also comes with its own set of considerations:

    - From the End: Removing an element from the end is typically 
      an $O(1)$ operation, as it doesn’t require repositioning of other elements.
    - From a Specific Index: Deletion from a particular index requires shifting 
    the subsequent elements to fill the gap, making it an $O(n)$ 
    time complexity operation.

1. Searching Elements

    Searching involves identifying the index of a specified element. 
    Without any additional information or constraints, a linear search is 
    performed, scanning each element until the sought one is found, 
    associating it with an $O(n)$ complexity. However, if the array is sorted, 
    binary search can be employed, reducing the complexity to $O(\log(n))$.

2. Updating Elements

    Updating an element at a specified index can be achieved directly 
    and is generally an $O(1)$ operation, since it entails altering 
    the value at a specified memory location, which is obtained without 
    scanning through additional elements.

## <span style="color:red">Những lưu ý về mảng khi tham gia phỏng vấn</span>

Nhìn array đơn giản như vậy, nhưng trong cuộc phỏng vấn có rất nhiều biến thể và
cạm bẫy có thể xảy ra. Luôn luôn hỏi người phỏng vấn về những điều sau:

1. **Validating Assumptions**:

- **Duplicates**: luôn luôn xác định mảng đầu vào có cho phép trùng lặp 
phần tử không. Hiểu và trao đổi về việc trùng lặp thì có "ảnh hưởng" gì 
đến cách giải của mình không.
- **Sorted/Unsorted**: Nếu mảng đã được sorted thì mình có thể áp dụng 
pattern Binary search

2. **Boundary Conditions**:

- **Index Out of Bounds**: Always ensure that your code never tries to access
an index outside of the array’s bounds. Use condition checks to prevent 
this common error.

- **Negative Indices**: In certain languages like Python, 
negative indices access elements from the end of the array. 
Be cautious and deliberate in your use of them.

3. **Efficiency Concerns**:

- **Slicing and Concatenating**: Remember slicing and concatenating can take 
$O(n)$ time. Be careful with these operations as they introduce significant 
time complexity into your solution.

- **In-place vs. Extra Space**: Consider whether creating a new array is 
necessary or if you can manipulate the existing array in place to save space.