<?php

echo "
<a href='orders_table.php'>
<input type='submit' value='Orders' />
</a>";

// Table for current unfilled orders
// https://stackoverflow.com/questions/17902483/show-values-from-a-mysql-database-table-inside-a-html-table-on-a-webpage
echo "<h2>Reservations To Check</h2>";
echo "<table border='1'>
<tr>
<th>Mountain</th>
<th>Month</th>
<th>Day</th>
<th>Year</th>
<th>Email</th>
</tr>";

// Fill table
$mysqli = new mysqli('localhost', 'root', '', 'mtnrez');

$result = $mysqli->query("SELECT * FROM reservationchecks");

while($row = $result->fetch_assoc()) {

	echo "<tr>";
	echo "<td>" . $row['mountain'] . "</td>";
	echo "<td>" . $row['month'] . "</td>";
	echo "<td>" . $row['day'] . "</td>";
	echo "<td>" . $row['year'] . "</td>";
	echo "<td>" . $row['email'] . "</td>";

	// add delete button and php reference
	echo "<td>
	<a href='deleteRes.php?mountain=".$row['mountain']
	."&month=".$row['month']."&day=".$row['day']."&year=".$row['year']
	."&email=".$row['email']."'>
	<input type='submit' value='Delete' class='btnDeleteAction' /></a>
	</td>";

	// add delete button and php reference
	echo "<td>
	<a href='../email.php'>
	<input type='submit' value='Email' class='btnDeleteAction' /></a>
	</td>";

	// end table row
	echo "</tr>";
}

?>
<HTML>
<HEAD>
<TITLE>Reservations To Check</TITLE>
<link href="../css/style.css" type="text/css" rel="stylesheet" />
<link rel="icon" href="../img/favicon.ico" type="image/ico">
</HEAD>
<BODY>
</BODY>
</HTML>