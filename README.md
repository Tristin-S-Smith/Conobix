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
