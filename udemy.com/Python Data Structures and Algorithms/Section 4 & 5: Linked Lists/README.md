# Linked List Fundamental

A list is in a contiguous place in memory => we can indexes and access 
through index for each element with time complexity: $O(1)$

Each element in Linked List(Node) are gonna be spread all over the place

## Singly Linked Lists vs Lists:

<table style="text-align: center">
  <thead>
    <tr>
      <th></th>
      <th>Linked Lists</th>
      <th>Lists</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Append</td>
      <td>O(1)</td>
      <td>O(1)</td>
    </tr>
    <tr>
      <td>Pop</td>
      <td  style="background: red">O(n)</td>
      <td  style="background: green">O(1)</td>
    </tr>
    <tr>
      <td>Prepend</td>
      <td style="background: green">O(1)</td>
      <td style="background: red">O(n)</td>
    </tr>
    <tr>
      <td>Pop First</td>
      <td style="background: green">O(1)</td>
      <td style="background: red">O(n)</td>
    </tr>
    <tr>
      <td>Insert</td>
      <td>O(n)</td>
      <td>O(n)</td>
    </tr>
    <tr>
      <td>Remove</td>
      <td>O(n)</td>
      <td>O(n)</td>
    </tr>
    <tr>
      <td>Look up by Index</td>
      <td style="background: red">O(n)</td>
      <td style="background: green">O(1)</td>
    </tr>
    <tr>
      <td>Look up by Value</td>
      <td>O(n)</td>
      <td>O(n)</td>
    </tr>
  </tbody>
</table>