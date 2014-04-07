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

    
    <?php
      error_reporting(0);
      session_start();  // Killing warning for this call.
      error_reporting(E_ERROR | E_WARNING | E_PARSE);
      $username = $_SESSION['username'];
      // connect
      $db_hostname = '127.0.0.1'; $db_database = 'ChoraleAnalyzerDB'; $db_username = 'calpeyser'; $db_password = 'charleb'; // some details
      $db_server = mysql_connect($db_hostname, $db_username, $db_password);
      if (!$db_server) die("Unable to connect to MySQL: " . mysql_error());

      // select
      mysql_select_db($db_database)
      or die("Unable to select database: " . mysql_error());

      // query
      $query = "SELECT * FROM chorales WHERE user = '$username'";
      $result = mysql_query($query);
      if (!$result) die ("Database access failed: " . mysql_error());
      $rows = mysql_num_rows($result);

    ?>


    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="jumbotron.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy this line! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>
  <?php session_start() ?>

    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">ChoraleAnalyzer</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form navbar-right" role="form" action="logout.php" method="POST">
            <button type="submit" class="btn btn-success">Logout</button>
          </form>
        </div><!--/.navbar-collapse -->
      </div>
    </div>

    <!-- Main jumbotron for a primary marketing message or call to action -->
    <div class="jumbotron">
      <div class="container">
        <h1><?php echo "Welcome, ".$_SESSION['username'] ?></h1>
        <p>Use this page to analyze your chorales for errors, and to track your long-term error profile.</p>
      </div>
    </div>

    <div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="col-md-4">
          <h2>Analyze a Chorale</h2>
          <p>Your input will be stored for later reference.</p>
          <form action="analyze.php" method="POST" enctype="multipart/for\
          m-data">
          <label for ="name">Please provide a name for your chorale:</label>
          <input type="text" name="name" id="name"><br>
          <label for="chorale">XML Formatted Chorale</label>
          <input type="file" name="chorale" id="chorale"><br>
          <label for="RNA">Romantext Formatted RNA</label>
          <input type="file" name="RNA" id="RNA"><br>
          <input type="submit" name="submit" value="Submit">
          </form>
        </div>
        <div class="col-md-4">
          <h2>View Your Chorales</h2>
          <?php
      // display
              echo "<B>Chorales in memory:</B> <BR>";
              echo "<SELECT NAME=\"Chorales\" SIZE=\"10\" MULTIPLE >";

              for ($j = 0; $j < $rows; ++$j)
              {
                echo "<OPTION>".mysql_result($result, $j, 'name'); 
              }

              echo "</SELECT>          </ul>";
          ?>
       </div>
        <div class="col-md-4">
          <h2>BLERG</h2
          <p>Blerg</p>
          <p><a class="btn btn-default" href="#" role="button">View details &raquo;</a></p>
        </div>
      </div>

      <hr>

      <footer>
        <p>Created by Charles Peyser, Princeton '15</p>
      </footer>
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
  </body>
</html>
