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
    <title>ChoraleAnalyzer - Romantext Format</title>

    <!-- Bootstrap core CSS -->
    <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">
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
	    <div class="jumbotron" align="center">
	    	<h1>Romantext Format</h1>
	    	<p align="left">While Dmitri Tymoczko’s romantext format for roman numeral analysis is yet to be documented in an easy to find place, it has the benefit of being extremely simple.  
			Romantext notation assigns each measure to a single line.  For each measure, each chord is enumerated by its beat within the measure followed by its roman numeral.   We also notate keys and key changes with upper case letters for major keys and lower case letters for minor keys.  Designation of a key must occur only at the beginning of a piece and at a key change.  Consider the following phrase:</p>
			<img border="0" src="pic1.png" alt="pic1" width="354" height="228">
			<p align="left"> In romantext format, we could write its roman numeral analysis as
			m0 b1 C: I b2 V b3 I b4 V 
			m1 b1 V b2 I
			The following list enumerates other details in the romantext format:
		<ul>
			<li align="left" style="line-height:150%">1.	Fractional beats are notated with a decimal after the beat number.  For example, a chord occurring on the fifth eighth note in a 4/4 measure would be denoted with b2.5; one occurring on the fifth sixteenth note would be denoted with b1.25.</li>
			<li align="left" style="line-height:150%">2.	First inversion is notated as expected: a first inversion I chord would be I6.  Other inversions (which involve more than one number) are notated with a “/”.  For example, a second inversion I chord would be I6/4, and a third inversion V7 chord would be V4/2.</li>
			<li align="left" style="line-height:150%">3.	Borrowed chords are also represented with “/”.  For example, a first inversion D7 chord in the key of C is V6/5/V.</li>
			<li align="left" style="line-height:150%">4.	Diminished chords are represented with an “o”, as in viio6.   Augmented chords are represented with a “+”.</li>  
			<li align="left" style="line-height:150%">5.	One may include multiple versions of an analysis.  For example, the following line occurs in Mia Tsui’s analysis of BWV 151.5:</li>
			m5 I b2 V4/3 b3 I6 b4 vi<br>
			m5var1 I b2 V4/3 b3 I6 b4 vi b4.5 IV6
			<li align="left" style="line-height:150%">6.	 Notes may be included in the analysis.  They appear on their own lines and begin with the designation “Note:”.
		</ul>
		</p>
			<p align="left">I found it easiest to learn this form of notation simply by inspection.  For that purpose, I’ve included here an analysis of Bach’s 24th Chorale, by Professor Tymoczko. </li>
		</p><br>
			<img border="0" src="pic2.png" alt="pic2" width="800" height="650">



	    </div>
	</div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="../../dist/js/bootstrap.min.js"></script>
  </body>
</html>
