

//code or boolean expression
module boolean(
	input X,Y,Z,W,
	output F
);
assign F=((!X&&!Z)||(!Y&&!Z)||(!X&&Y)+(X&&Z&&W));

	endmodule
