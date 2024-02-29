#!/usr/bin/perl
use strict;
use warnings;

my $message = "just another perl hacker";
my $output = "";

for my $char (split //, $message) {
    my $ord = ord($char);
    $output .= sprintf("&#%d;", $ord);
}

print $output;
