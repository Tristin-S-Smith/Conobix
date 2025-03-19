<h1>Conobix</h1>
<h3>The Conditional Object Matrix Esolang</h3>
<p>Conobix is an esolang that (as the extended abbreviation implies) is built around a matrix of objects called <strong>Conobi</strong>. This matrix is then mirrored by a matrix of equal dimensions to store values.</p>

<h2>Defining Conobi</h2>
<p>Conobix is a language that is split into chunks by section headers. All Conobi are defined under the <em>~DEFINE~</em> section header. They are defined as follows:</p>
<code>[symbol] | [mutate]/[condition1]/[condition2]/[condition3]/[condition4]</code>

<p>The <em>symbol</em> parameter is what the Conobi will be represented as. The <em>mutate</em> parameter is how the data passed to a Conobi is modified. The mutate parameter will take a three-letter operation and a value. The following operations are available:</p>

<table>
<tr>
<th> Operation</th> <th>Name</th><th>Description</th>
</tr>
<tr>
<th> add[n]</th> <th>Add</th><th>Add n to the value of the current Conobi </th>
</tr>
<tr>
<th> sub[n]</th> <th>Subtract</th><th>Subtract n to the value of the current Conobi </th>
</tr>
<tr>
<th> mul[n]</th> <th>Multiply</th><th>Multiply the value of the current Conobi by n </th>
</tr>
<tr>
<th> div[n]</th> <th>Divide</th><th>Divide the value of the current Conobi by n </th>
</tr>
<tr>
<th> exp[n]</th> <th>Exponent</th><th>Raise the value of the current Conobi to the n<sup>th</sup> power </th>
</tr>
<tr>
<th> out[n]</th> <th>Output</th><th>Convert the value of the current Conobi to ASCII and output it n times</th>
</tr>
</table>

<p>The <em>condition1-4</em> parameters will decide what direction the current Conobi will pass its data. Conditions 1-4 will pass data in the North, East, South, and West directions respecively. The conditions will also be checked in that order. The condition parameters will take a two-letter comparison and a value. The following comparisons are available:</p>

<table>
<tr>
<th> Comparison</th> <th>Name</th><th>Description</th>
</tr>
<tr>
<th> gt[n]</th> <th>Greater than</th><th>Check if the value of the current Conobi is greater than n</th>
</tr>
<tr>
<th> lt[n]</th> <th>Less than</th><th>Check if the value of the current Conobi is less than n</th>
</tr>
<tr>
<th> ge[n]</th> <th>Greater than or equal to</th><th>Check if the value of the current Conobi is greater than or equal to n</th>
</tr>
<tr>
<th> le[n]</th> <th>Less than or equal to</th><th>Check if the value of the current Conobi is less than or equal to n</th>
</tr>
<tr>
<th> eq[n]</th> <th>Equal to</th><th>Check if the value of the current Conobi is equal to n </th>
</tr>
<tr>
<th> ne[n]</th> <th>Not equal to</th><th>Check if the value of the current Conobi is not equal to n</th>
</tr>
</table>

<p>There are also two special comparisons available for the condition parameters. These comparisons do not take a value. They are as follows:</p>

<table>
<tr>
<th> Comparison</th> <th>Name</th><th>Description</th>
</tr>
<tr>
<th> ~</th> <th>Always false</th><th>Return false no matter what </th>
</tr>
<tr>
<th> ?</th> <th>Always true</th><th>Return true no matter what</th>
</tr>
</table>