<!DOCTYPE html>


<?php
// validation of username and password, insertion into database
require_once ( 'newaccount.php' );
$homepage = "localhost";

// check that the form has been filled out
if (isset($_POST['newusername']) and isset($_POST['newpassword']) and isset($_POST['newpassword2'])) {
	if($_POST['newusername'] != "" and $_POST['newpassword'] != "" and $_POST['newpassword2'] != "") {
		// check that newpassword == newpassword2
		if ($_POST['newpassword'] != $_POST['newpassword2']) {
			echo "Password entries must match - please try again";
			goto renderPage;
		}
		// check that username doesn't already exist
		// connect

    // from http://www.pontikis.net/blog/how-to-use-php-improved-mysqli-extension-and-why-you-should
    $DBServer = '127.0.0.1';
    $DBUser = 'calpeyser';
    $DBPass = 'charleb';
    $DBName = 'ChoraleAnalyzerDB';
    $conn = new mysqli($DBServer, $DBUser, $DBPass, $DBName);
    if (mysqli_connect_errno()) {
      trigger_error('Database connection failed: ' . mysqli_connct_error(), E_USER_ERROR);
    }


		//$db_hostname = '127.0.0.1'; $db_database = 'ChoraleAnalyzerDB'; $db_username = 'calpeyser'; $db_password = 'charleb'; // some details
		//$db_server = mysql_connect($db_hostname, $db_username, $db_password);
		//if (!$db_server) die("Unable to connect to MySQL: " . mysql_error());

		// select
		//mysqli_select_db($db_database)
		//or die("Unable to select database: " . mysqli_error());

		// query
		$query = "SELECT * FROM users";
		$rs = $conn->query($query);

    if($rs === false) {
    trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
    } else {
      $rows_returned = $rs->num_rows;
    }

		//if (!$result) die ("Database access failed: " . mysqli_error());
		//$rows = mysqli_num_rows($result); // all the usernames
		//for ($j = 0; $j < $rows; ++$j)
		//{
		//	if (mysqli_result($result, $j, 'username') == $_POST['newusername']) {
		//		print "We're sorry, " . $_POST['newusername'] . " is already in use. Please choose another username and try again.";
		//		goto renderPage;
		//	}
		//}

    $rs->data_seek(0);
    while($row = $rs->fetch_assoc()){
      if ($row['username'] == $_POST['newusername']) {
        print "We're sorry, " . $_POST['newusername'] . " is already in use. Please choose another username and try again.";
        goto renderPage;
      }
    }

    $newusername = $_POST['newusername'];
    $newpassword = $_POST['newpassword'];

    $v1="'" . $conn->real_escape_string("$newusername") . "'";
    $v2="'" . $conn->real_escape_string("$newpassword") . "'";
     
    $sql="INSERT INTO users (username, password) VALUES ($v1,$v2)";
     
    if($conn->query($sql) === false) {
      trigger_error('Wrong SQL: ' . $sql . ' Error: ' . $conn->error, E_USER_ERROR);
    } else {
      $last_inserted_id = $conn->insert_id;
      $affected_rows = $conn->affected_rows;
    }


		// we know this username dosen't already exist, so we can add it to the database
//		$newusername = $_POST['newusername'];
//		$newpassword = $_POST['newpassword'];
//		$query = "INSERT INTO users (username, password) VALUES ('$newusername', '$newpassword')";
//		$result2 = mysqli_query($query);
//		if (!$result2) die ("Problem putting new username and password into database: " . mysqli_error());
//		header("Location: http://$homepage");
	}
	else {
		echo "Please fill out the entire form.";
	}
}
	
renderPage:
?>

<html lang="en">
  <head>

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

    <title>ChoraleAnalyzer - Create an Account</title>

    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href=<?php echo "http://$homepage" ?> >ChoraleAnalyzer</a>
          <a class="navbar-brand" href=<?php echo "http://$homepage/ChoraleAnalyzer/about.php" ?>>About</a>
        </div>
        <div class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">

      <div class="starter-template">
        <h1>Welcome Aboard!</h1>
        <p class="lead">By creating an account on ChoraleAnalyzer.com, you allow yourself to store graded chorales for later inspection.<br>You will also be able to access statistical analysis of any body of chorales that you have submitted.</p>
      </div>

        <form action="" method="POST" enctype="multipart/for\
          m-data">
        <label for="username">Username:</label>
        <input type="text" name="newusername" id="newusername"><br>
        <label for="password">Password:</label>
        <input type="text" name="newpassword" id="newpassword"><br>
        <label for="password2">Confirm Password:</label>
        <input type="text" name="newpassword2" id="newpassword2"><br>

        <input type="submit" name="submit" value="Create Account">
        </form>


    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
  </body>
</html>
