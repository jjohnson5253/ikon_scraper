<?php

$mysqli = new mysqli('localhost', 'root', '', 'mtnrez');

$sql = "INSERT INTO reservationchecks(mountain, month, day, 
					year, email) VALUES
				 ('".$_POST["mountain"]."','".$_POST["month"]."','".$_POST["day"]."'
				 	,'".$_POST["year"]."','".$_POST["email"]."')";

if ($mysqli->query($sql) === TRUE){
	echo "You have successfully registered.";

	echo "
	<a href='login.php'>
	<input type='submit' value='Login' />
	</a>";
} else {
	echo "error: " . $sql . "<br><br>" . $mysqli->error;
}

?>

<html>
<TITLE>Confirmation</TITLE>
<body>


</body>
</html>