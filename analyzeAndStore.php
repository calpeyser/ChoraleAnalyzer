<?php

// This script has to do two things: store the chorale in the database and analyze the chorale for the user

error_reporting(E_ALL);
ini_set('display_errors', '1');

// homepage
$homepage = "localhost";

// get the username
error_reporting(0);
session_start();  // Killing warning for this call.
error_reporting(E_ERROR | E_WARNING | E_PARSE);
$username = $_SESSION['username'];

// check that the form has been filled out
if (isset($_POST['name']) and isset($_FILES['chorale']) and isset($_FILES['RNA'])) {
	if($_POST['name'] != "") {

		// get data from the form
		$name = $_POST['name'];
		$chorale_temp_name = $_FILES["chorale"]["tmp_name"];
		$rna_temp_name = $_FILES["RNA"]["tmp_name"];

		$chorale_fp = fopen($chorale_temp_name, "r");
		$rna_fp = fopen($rna_temp_name, "r");

		$xml = fread($chorale_fp, filesize($chorale_temp_name));
		$rna = fread($rna_fp, filesize($rna_temp_name));

	    // from http://www.pontikis.net/blog/how-to-use-php-improved-mysqli-extension-and-why-you-should
	    // Connect to the database
	    $DBServer = '127.0.0.1';
	    $DBUser = 'calpeyser';
	    $DBPass = 'charleb';
	    $DBName = 'ChoraleAnalyzerDB';
	    $conn = new mysqli($DBServer, $DBUser, $DBPass, $DBName);
	    if (mysqli_connect_errno()) {
	      trigger_error('Database connection failed: ' . mysqli_connct_error(), E_USER_ERROR);
	    }


	    // check that this name isn't already taken
	    $query = "SELECT * FROM chorales";
		$rs = $conn->query($query);
		$rs->data_seek(0);
	    while($row = $rs->fetch_assoc()){
	      if ($row['username'] == $username) {
	      	if ($row['name'] == $name) {
	        header("Location: http://$homepage/ChoraleAnalyzer/profile.php?nameunique=$name");
	        exit;
	    	}
	      }
	    }


		// call the backend to do the analysis, and store the result
		$output = array();
		$s = shell_exec("python copyFiles.py $arg1 $arg2");
		exec("python printAnalysis.py xmlfile.xml rnafile.txt 2> out", $output);

		// read the pickle file
		$errTracker_fp = readfile("error_tracker.pkl");
		$errTracker    = fread($errTracker_fp, filesize("error_tracker.pkl"));

		// let's add this chorale to the database
	    $v1="'" . $conn->real_escape_string("$name") . "'";
	    $v2="'" . $conn->real_escape_string("$username") . "'";
	    $v3="'" . $conn->real_escape_string("$xml") . "'";
	    $v4="'" . $conn->real_escape_string("$rna") . "'";
	    $v5="'" . $conn->real_escape_string("$errTracker"). "'";


		$sql="INSERT INTO chorales (name, username, xml, rna, errorTracker) VALUES ($v1, $v2, $v3, $v4, $v5)";

	    if($conn->query($sql) === false) {
	      trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
	    } else {
	      $last_inserted_id = $conn->insert_id;
	      $affected_rows = $conn->affected_rows;
	    }	
	    //header("Location: http://$homepage/ChoraleAnalyzer/profile.php");
	    print_r($output);
	}
	else header("Location: http://$homepage/ChoraleAnalyzer/profile.php");
	exit;
}
else {
		header("Location: http://$homepage/ChoraleAnalyzer/profile.php");
}
exit;



// copy the files, and do the analysis
$arg1 = $_FILES["chorale"]["tmp_name"];
$arg2 = $_FILES["RNA"]["tmp_name"];

$output = array();

$s = shell_exec("python copyFiles.py $arg1 $arg2");
echo $s;
//exec("python printAnalysis.py xmlfile.xml rnafile.txt 2> out", $output);
print_r($output); // replace this with a printing script?
?>