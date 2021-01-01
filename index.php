<?php

echo "<h1>Ikon Mountain Reservation Dates</h1>
	<h3>Dates Available</h3>
	<table border='1'>
	<tr>
	<th>Mountain</th>
	<th>Month</th>
	<th>Day</th>
	<th>Year</th>
	</tr>";

// Fill table
$mysqli = new mysqli('localhost', 'website', 'hugoboss123!', 'mtnrez');

$result = $mysqli->query("SELECT * FROM datesavailable");

while($row = $result->fetch_assoc()) {
	echo "<tr>";
	echo "<td>" . $row['mountain'] . "</td>";
	echo "<td>" . $row['month'] . "</td>";
	echo "<td>" . $row['day'] . "</td>";
	echo "<td>" . $row['year'] . "</td>";
	echo "</tr>";
}
echo "</table>";

?>

<HTML>
<HEAD>
<TITLE>Ikon Scraper</TITLE>
<link href="../css/style.css" type="text/css" rel="stylesheet" />
<link rel="icon" href="../img/favicon.ico" type="image/ico">
</HEAD>
<BODY>
</BODY>
</HTML>
