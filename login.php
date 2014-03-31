<html>
<body>
<h1>Login Page</h1>

<?php
// fetch data from form
$postedUsername = $_POST["username"];
$postedPassword = $_POST["password"];


// taking a lot of this from the book
// connect
$db_hostname = '127.0.0.1'; $db_database = 'ChoraleAnalyzerDB'; $db_username = 'calpeyser'; $db_password = 'charleb'; // some details
$db_server = mysql_connect($db_hostname, $db_username, $db_password);
if (!$db_server) die("Unable to connect to MySQL: " . mysql_error());

// select
mysql_select_db($db_database)
or die("Unable to select database: " . mysql_error());

// query
$query = "SELECT * FROM users";
$result = mysql_query($query);
if (!$result) die ("Database access failed: " . mysql_error());
$rows = mysql_num_rows($result);

// display
for ($j = 0; $j < $rows; ++$j)
{
  if (mysql_result($result, $j, 'username') == $postedUsername) {
  	if (mysql_result($result, $j, 'password') == $postedPassword) {
  		echo "found a match!";
  	}
  }
}

?>

</body>
</html>