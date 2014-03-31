<?php

error_reporting(E_ALL);
ini_set('display_errors', '1');

$arg1 = $_FILES["chorale"]["tmp_name"];
$arg2 = $_FILES["RNA"]["tmp_name"];

#$data1 = file_get_contents($arg1);
#$data2 = file_get_contents($arg2);


#file_put_contents("/var/www/html/xmlfile.xml", $data1);
#file_put_contents("/var/www/html/rnafile.txt", $data2);


$output = array();

$s = shell_exec("python copyFiles.py $arg1 $arg2");
echo $s;
exec("python ChoraleAnalyzer/printAnalysis.py xmlfile.xml rnafile.txt 2> out", $output);
print_r($output);
?>