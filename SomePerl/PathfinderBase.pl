#!/usr/bin/perl
use strict;
use warnings;

my @first_names = ("Aldric", "Elysia", "Thorn", "Isolde", "Garrick");
my @last_names  = ("Stoneforge", "Moonshadow", "Fireheart", "Stormrider", "Ironclaw");

my $random_first = $first_names[rand @first_names];
my $random_last  = $last_names[rand @last_names];

print "Random Pathfinder Character Name: $random_first $random_last\n";
