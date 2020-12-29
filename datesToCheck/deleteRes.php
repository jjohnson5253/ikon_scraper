<?php

// retrieve reservation to delete
$mountain = $_GET['mountain'];
$month = $_GET['month'];
$day = $_GET['day'];
$year = $_GET['year'];
$email = $_GET['email'];

// open connection
$mysqli = new mysqli('localhost', 'yourmom', 'Yourmom123!', 'mtnrez');

// TODO: change all sql queries to use this method to avoid sql injections:
$query = "DELETE FROM reservationchecks WHERE mountain = ? AND month = ? AND day = ? AND year = ? AND email = ?";
$stmt = $mysqli->prepare($query);

$stmt->bind_param('sssss', $mountain, $month, $day, $year, $email);
$stmt->execute();

// close connection
mysqli_close($mysqli);

// stay on orders_table.php
header('Location: reservations.php');

?>
