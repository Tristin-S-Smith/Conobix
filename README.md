<h1>Conobix</h1>
<h3>The Conditional Object Matrix Esolang</h3>
<p>Conobix is an esolang that (as the extended abbreviation implies) is built around a matrix of objects called <strong>Conobi</strong>. This matrix is then mirrored by a matrix of equal dimensions to store values.</p>

<h2>Defining Conobi</h2>
<p>Conobix is a language that is split into chunks by section headers. All Conobi are defined under the <em>~DEFINE~</em> section header. They are defined as follows:</p>
<code>[symbol] | [mutate]/[condition1]/[condition2]/[condition3]/[condition4]</code>

<p>The <em>symbol</em> parameter is what the Conobi will be represented as. The <em>mutate</em> parameter is how the data passed to a Conobi is modified. The mutate parameter will take a three-letter operation and a value. The following operations are available:</p>


