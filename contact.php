<!DOCTYPE html>

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

    <title>ChoraleAnalyzer - About</title>

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

  <?php $homepage = "localhost" ?>


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
        <h1>Contact: Charles Peyser, Princeton '15</h1>
        <p class="lead">Please get in touch with bugs, questions, or comments.</p>
      </div>

      <!-- http://tangledindesign.com/how-to-create-a-contact-form-using-html5-css3-and-php/ -->
      <section class = "body">

        <form method = "POST" action = "sendEmail.php">
                
            <label>Name</label>
            <input name="name" placeholder=""><br>
                    
            <label>Email</label>
            <input name="email" type="email" placeholder=""><br>
                    
            <label>Message</label><br>
            <textarea name="message" placeholder="" maxlength = 10000 cols = "25" rows= "10"></textarea><br>
                    
            <input id="submit" name="submit" type="submit" value="Submit">
                
        </form>
      </section>


    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
  </body>
</html>
