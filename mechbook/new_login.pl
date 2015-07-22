#!/usr/bin/perl
use strict;
use warnings;
use WWW::Mechanize;
use HTTP::Cookies::Netscape; #you were using two times use
my $cookies='your cookies file path';
my $mech = WWW::Mechanize->new( cookie_jar => HTTP::Cookies::Netscape->new( file => $cookies) );
$mech->agent_alias('Windows Mozilla'); #this is right user agent
$mech->get("https://www.facebook.com/login.php");
$mech->submit_form(
fields => {
    email =>'your username',
    pass => 'your password',
   }
);

open(my $out, ">",  "output_page.html") or die "Can't open output_page.html: $!"; #make lexical variables using my
print $out $mech->content;
