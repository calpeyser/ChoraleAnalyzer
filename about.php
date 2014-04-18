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

      <div class="jumbotron">
        <h1>ChoraleAnalyzer:<br> <b>Automatic Bach-Style Chorale Analysis and Grading</b></h1>
      </div>
      <div class="jumbotron">
        <h3 align="center">What it does</h3>
        <p>ChoraleAnalyzer is a program that validates a chorale for conformity with specific Bach rules. It is motivated by the 
          tedium of the grading process for beginner and intermediate level music theory classes.  The tool is meant to be used by
          teachers to automate the grading of large groups of chorales.  The tool is capable of remembering the error profile of 
          submitted chorales to provide instructors with objective feedback on the strengths and weeknesses of a group of 
          students. </p>
        <p>The ChoraleAnalyzer tool needs two files in order to produce an analysis.  The user must provide: </p>
        <ul>
        <li style="line-height:150%"><b>A Chorale</b>: ChoraleAnalyzer understands the <a href="http://www.musicxml.com/">MusicXML format</a> 
          (.xml) for musical notation. Most modern musical notation softwares support MusicXML in either their standard
          distribution of in a downloadable extention.  The use of MusicXML allows for easy parsing of the chorale for
          computation. </li>
        <li style="line-height:150%"><b>A Roman Numeral Analysis</b>: Unfortunately, there exists no standard digital format for Roman
          Numeral Analysis.  ChoraleAnalyzer uses the <a href=<?php echo "http://$homepage/ChoraleAnalyzer/romantext.php"?>>
          romantext format</a>.</li>
        </ul>
      </div>

      <div class="jumbotron">
        <h3 align="center">How it works</h3>
        <p>On the backend, ChoraleAnalyzer is a set of programs, written in Python, that check a chorale for one error type in 
        particular.  The tool is architected such that each program is in run on a submitted chorale and roman numeral analysis, while
        output is stored and eventually printed. </p>
        <p>Three broad catagories of tests are conducted </p>
        <ul>
        <li style="line-height:150%">1) <b>Chorale-centric checks</b>, which use only the musicXML file.  These include:
            <ul>
              <li style="line-height:150%">Parallel Intervals – checks for parallel unisons, fifths, and octaves</li> 
              <li style="line-height:150%">Voice Leading – checks for other violations involving a pair of adjacent chords.  Includes checks for tritones  and repeated bass tones .</li>
              <li style="line-height:150%">Zero Order – checks involving only one chord.  Includes validation of part ranges , distance between parts , and voice crossings .</li>
            </ul>
        </li>
        <li style="line-height:150%">2)  <b>Checks relevant to the roman numeral analysis</b>, which use only the romantext file.  These include :
            <ul>
              <li style="line-height:150%">Validation that chords of correct modality are used, given the key.</li>
              <li style="line-height:150%">Checks for incorrect progressions, ex. V to IV.</li>  
              <li style="line-height:150%">Checks that appropriate chord inversions are used.</li>
            </ul>
        </li>
        <li style="line-height:150%">3)  <b>Roman Numeral Analysis validation</b>, which compares the musicXML file to the romantext file and points out inconsistencies.  
        </li>
        </ul>
      </div>

      <div class="jumbotron">
        <h3 align="center">The scoring mechanism</h3>
        <p>In addition to the results of the checks, the program prints a “Bachness” score for the chorale.  A chorale’s Bachness is a numerical metric that seeks to give the degree to which the chorale is consistent with the Bach rules.  The Bach chorales on average have a Bachness of 1; scores greater than 1 indicate a chorale which violates the Bach rules more often than the chorales themselves and visa versa.
The computation of the Bachness score requires data on the chorales themselves, which was collected by running the program on the first 70 Bach chorales , comprising 1006 measures of music. 
</p>
        <p>These data provide the foundation for the Bachness computation.  For any chorale, the program tallies up errors and produces a similar chart, tracking average violations per measure and comparing it to the data on the Bach chorales themselves.  The program then computes the ratio of violations per measure in the student chorale to violations per measure in Bach for each individual error type (errors which occurred zero times are approximated as having occurred once, to avoid division by zero).  Averaging these ratios gives the submission’s Bachness. </p>
      </div>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
  </body>
</html>
