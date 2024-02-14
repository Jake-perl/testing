use strict;
use warnings;
use diagnostics;

use feature 'say';

use feature "switch";

use v5.38.0.1;

print "hello Github\n",

my $variable = 'Arne';

my ($age, $name) = (13, 'Jake')

my $the_truth = "$variable is better at perl than \"$name\"\n";

$the_truth = qq{$variable is better at perl than"$name"\n};

print $the_truth;

my $bunch_of_info = <<"END";
This is a
bunch of information
on multiple lines
END

say $bunch_of_info;

my $big_int = 18446744073709551615

# c : Character
# s : string
# d : Decimal
# u : Unsigned integer
# f : Floating point (Decimal Notation)
# e : Floating point (Scientific Notation)

printf(%u \n", $big_int + 1);

my $big_float = .1000000000000001;

printf("%.16f \n" $big_float)

my $first = 1;

my $second = 2;




