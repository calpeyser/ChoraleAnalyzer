<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Chorale Analyzer</title>

        <!-- Obtain Bootstrap style sheet from CDN (online service) so it doesn't have to be on my machine -->
  <!-- Check http://www.bootstrapcdn.com/ for latest version. -->
  <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
   <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
        font-family:"Palatino Linotype", "Book Antiqua", Palatino, serif;

      }
    </style>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="../../assets/ico/favicon.ico">

    

    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">

<?php
// where is the homepage?
$homepage = "localhost";
$loggedin = False;


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
  		// consider SALTing passwords
  		$loggedin = mysql_result($result, $j, 'username');
  	}
  }
}
if (!$loggedin) header("Location: http://$homepage?loginattempt=failed");
else {
	session_start();
	$_SESSION['username'] = $loggedin;
	header("Location: http://$homepage/ChoraleAnalyzer/profile.php");
}
?>


