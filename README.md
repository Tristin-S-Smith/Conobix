<h1>Conobix</h1>
<h3>The Conditional Object Matrix Esolang</h3>
<p>Conobix is an esolang that (as the extended abbreviation implies) is built around a matrix of objects called <strong>Conobi</strong>. This matrix is then mirrored by a matrix of equal dimensions to store values.</p>

<h2>Defining Conobi</h2>
<p>Conobix is a language that is split into chunks by section headers. All Conobi are defined under the <em>~DEFINE~</em> section header. They are defined as follows:</p>
<code>[symbol] | [mutate]/[condition1]/[condition2]/[condition3]/[condition4]</code>
<p></p>

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
<br>

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
<br>

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
<br>

<p>The following is an example of a Conobi represented by @. After it receives data, it will add 20 to it. Afterwards, the Conobi will compare its data to four conditions to determine what direction to send it. The Conobi will send the data North if it is equal to 16. It will never send the data East. It will send the data South if it is less than 4. If none of these conditions are met, it will always send the data West.</p>
<code>~DEFINITION~
@ | add20/eq16/~/lt4/?</code>

<h2>Arranging Conobi</h2>
<p>The layout of a Cobix program is not like that of your standard Imperative Programming Language. Instead, Conobi are arranged into a matrix under the <em>~SCHEMATIC~</em> section header. The position of defined Conobi in this matrix tie pack to the aforemention direction data is passed with the condition parameters. It is highly reccomended to create a matrix with an equal width and height, as well as fill any blank characters with a specified null character.</p>
<p>Assuming !, @, #, and $ are defined Conobi, a valid matrix would look like:</p>
<code>~SCHEMATIC~
!@
#$
</code>
<p></p>
<p>Keep in mind, the matrix can be any width and any height. Conobi within the matrix can also be reused as many times as desired.</p>
<p>To terminate a Conobix program, either access a Conobi that is not defined within the matrix, or pass data to an all-false Conobi (passing data to a Conobi and having all four condition parameters return false will terminate the program).</p>

<h2>Executing a Conobi Matrix</h2>
<p>Where Conobix starts executing in the matrix, and the initial value to pass to the specified Conobi are defined in the <em>~EXECUTE~</em> section header. The arrangement for this data is:</p>
<code>[x]/[y]/[data]</code>
<p></p>

<p>The x and y parameters define the starting x and y values for the program. The data parameter stores any decimal value to be passed into the first Conobi.</p>
<p>Telling the Conobix program to start at position (2,3) in the matrix with an initial data pass of 48 would resemble:</p>
<code>~EXECUTE~
2/3/48
</code>

<h2>Program Flags</h2>
<p>Program Flags are specific rules set at the beginning of a Conobix program that will change the functionality of the Conobix interpreter itself. Program flags are denoted by a <em>?</em>, and they can be placed anywhere before the <em>~DEFINE~</em> section header. They are defined as follows:</p>
<code>?[flag]
~DEFINE~
</code>
<p></p>
<p> The <em>flag</em> parameter specifies which flag will be set. The following flags are available:</p>

<table>
<tr>
<th> Flag</th> <th>Name</th><th>Description</th>
</tr>
<tr>
<th> NULLEXEC</th> <th>Null execution</th><th> Execute the program with both the starting coordinates and the starting value set to 0. When this flag is present, neither <em>~EXECUTE~</em> nor the content under it will need to be in the program. If it is present, it will be ignored in favor of 0/0/0.</th>
</tr>
<tr>
<th> STROUT</th> <th>String out</th><th>Modify the behavior of the <em>out[n]</em> mutate parameter to output the actual number within its Conobi rather than converting the number to ASCII and outputting it.</th>
</tr>
<tr>
<th> LNBRK</th> <th>Line break</th><th>Modify the behavior of the <em>out[n]</em> mutate parameter to output on a new line each time it is called instead of outputting everything on the same line.</th>
</tr>
</table>


<h2>Misc. Functionality</h2>
<p> A comment can be made in any section using ` at the start. It is crucial that comments are made on their own specific line. No instructions should come before or after the comment on the same line.</p>
<code>`This is a comment</code>
<p></p>
<p>It was mentioned previously that it might be a good idea to implement an all-false Conobi to halt the program if an out-of-bounds Conobi isn't easily accessible. The following is an example of an all-false Conobi:</p>
<code>! | add0/~/~/~/~</code>
<p></p>
<p>To execute a Conobix program, run <em>conobix.py</em> and input the file path to your program.

