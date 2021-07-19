public static int calcDiv (int dividendo, int divisor){
		if (dividendo<divisor){
			return 0;
		}
		
		return 1+calcDiv(dividendo-divisor, divisor);
	}