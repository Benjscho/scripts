#!/usr/bin/awk -f
# Author: Katef
# Source: https://gist.github.com/katef/f52978b2ba4583d195414f19342d91ca

function hoop(h, w) {
	printf("l 0 %d ", -h);
	printf("c 0 -%u, %u -%u, %u 0 ", w, w, w, w);
	printf("l 0 %d", +h);
}

function hand(x, h, o, l) {
	printf("<g transform='translate(%d.5 %d)'>\n", x, h);
	for (a = 0; a < 5; a++) {
		printf("  <g transform='rotate(-%u)'>\n", a * 15 + o);

#		printf("<circle cx='0' cy='0' r='1' fill='white'/>\n");

		printf("    <path d='M 0 -8 ");
		hoop(l, 2);
		printf("'/>\n")
		printf("  </g>\n");
	}
	printf("</g>\n");
}

function eye(x, y) {
	printf("  <circle cx='%d' cy='%d' r='1'/>\n", x, y);
}

function hattifattener(w, h1, h2, l, ed,    gap) {
	gap = w

#	printf("<circle cx='0' cy='0' r='2' fill='white'/>\n");

	printf("  <path d='M %u %u ", 0, 0);
	printf("l 0 %d m 0 %d", -h1, -gap);
	hoop(h2, w);
	printf("m 0 %d l 0 %d", gap, h1);
	printf("'/>\n")

	hand(w - 4, -h1 - gap / 2, 65, l);
	hand(w - 7, -h1 - gap / 2, 65 + 180, l);

	ed /= 2
	eye(w - 3 - ed, -h1 - h2 - gap - 2 - ed);
	eye(w - 6 - ed, -h1 - h2 - gap - 2 - ed);
}

BEGIN {
	print "<?xml version='1.0' encoding='UTF-8' standalone='no'?>"
	print ""

	print "<svg"
	print "   xmlns='http://www.w3.org/2000/svg'"
	print "   width='200mm'"
	print "   height='60mm'"
	print "   viewBox='0 -60 200 70'"
	print "   version='1.1'>"
	print ""

	print "  <style>path, circle { fill: #272222; stroke: white; stroke-width: 0.4; }</style>"
	print ""

}

{
	srand(seed + $1)

	printf("<g transform='rotate(%d) translate(%u %u)'>",
		rand() * 5 - 3,
		rand() * 200, rand() * 2);
	hattifattener(10, 5 + rand() * 20, 5 + rand() * 20, rand() * 10, rand() * 3 - 1)
	print "</g>"
}

END {
	print "</svg>"
}
