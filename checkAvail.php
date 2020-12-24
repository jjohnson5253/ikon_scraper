
<?php

$checkAvailCmd = escapeshellcmd('python\main.py Snoopy123! '.$_POST["month"]
	.' '.$_POST["day"].' '.$_POST["year"]);
$output = shell_exec($checkAvailCmd);
echo $output;

?>

<html>
<TITLE>Availability</TITLE>
<body>



</body>
</html>