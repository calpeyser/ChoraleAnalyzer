<?php
	//http://tangledindesign.com/how-to-create-a-contact-form-using-html5-css3-and-php/
	$name = $_POST['name'];
	$email = $_POST['email'];
	$message = $_POST['message'];

	$body = "From: $name, Email: $email, Content: $message";

	if ($_POST['submit']) {
		if (mail("peyser@princeton.edu", "Message from ChoraleAnalyzer.com", $body, "ContactForm")) {
			echo '<p>Your message has been sent.  Thanks for getting in touch!</p>';
		}
		else {
			echo '<p>I\'m sorry, your message did not go through.</p>';
		}
	} 
?>