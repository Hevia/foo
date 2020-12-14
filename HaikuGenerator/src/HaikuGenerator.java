import java.util.ArrayList;
import java.util.Random;


public class HaikuGenerator 
{
	//public void haikuGen();
	
	public static void main(String[] args) 
	{
		String[] oneSyllableWords = {"go", "po", "hi", "dog", "boom", "kit", "mom", "is", "math", "word", "poop", "build", "his"};
		String[] twoSyb = {"mental", "lemur", "comcast", "kitkat", "gundam", "seconds", "station", "rasins"};
		String[] threeSyb = {"Sengoku", "terrible"};
		String[] fourSyb = {"terrifying"};

		int oneSyllable = 1;
		int twoSyllables = 2;
		int threeSyllables = 3;
		int fourSyllables = 4;
		int fiveSyllables = 4;
		
		int lineUno = 5;
		int lineDos = 7;
		int lineTres = 5;
		Random rGenerator = new Random();

		
		ArrayList<String> haikuLine1 = new ArrayList<String>();
		ArrayList<String> haikuLine2 = new ArrayList<String>();
		ArrayList<String> haikuLine3 = new ArrayList<String>();
		
		int currentSybCounter = 0;
		int currentSybSelection = 0;
	//----------------------------------------------------------------------------------------------	
		for(int i = 0; i < lineUno; i++)
		{
			currentSybSelection = rGenerator.nextInt(lineUno);
			if(currentSybCounter == 4)
			{
				currentSybCounter = currentSybCounter + 1;
				haikuLine1.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
			}	
			if(currentSybCounter + currentSybSelection <= lineUno)
			{
				if(currentSybSelection == oneSyllable)
				{
				currentSybCounter = currentSybCounter + 1;
				haikuLine1.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
				}
				if(currentSybSelection == twoSyllables)
				{
				currentSybCounter = currentSybCounter +2;
				haikuLine1.add(twoSyb[rGenerator.nextInt(twoSyb.length)]);	
				}	
				if(currentSybSelection == threeSyllables)
				{
				currentSybCounter = currentSybCounter + 3;
				haikuLine1.add(threeSyb[rGenerator.nextInt(threeSyb.length)]);		
				}	
				if(currentSybSelection == fourSyllables)
				{
				currentSybCounter = currentSybCounter + 4;
				haikuLine1.add(fourSyb[rGenerator.nextInt(fourSyb.length)]);	
				}	
			} else 
			{
			   i--;
			}
		}
		System.out.println(haikuLine1);
		
		
		//----------------------------------------------------------------------------------------------	
		currentSybCounter = 0;
		currentSybSelection = 0;
		for(int i = 0; i < lineDos; i++)
		{
			currentSybSelection = rGenerator.nextInt(lineDos);
			if(currentSybCounter == 6)
			{
				currentSybCounter = currentSybCounter + 1;
				haikuLine2.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
			}	
			if(currentSybCounter + currentSybSelection <= lineDos)
			{
				if(currentSybSelection == oneSyllable)
				{
				currentSybCounter = currentSybCounter + 1;
				haikuLine2.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
				}
				if(currentSybSelection == twoSyllables)
				{
				currentSybCounter = currentSybCounter +2;
				haikuLine2.add(twoSyb[rGenerator.nextInt(twoSyb.length)]);	
				}	
				if(currentSybSelection == threeSyllables)
				{
				currentSybCounter = currentSybCounter + 3;
				haikuLine2.add(threeSyb[rGenerator.nextInt(threeSyb.length)]);		
				}	
				if(currentSybSelection == fourSyllables)
				{
				currentSybCounter = currentSybCounter + 4;
				haikuLine2.add(fourSyb[rGenerator.nextInt(fourSyb.length)]);	
				}	
			} else {
			   i--;
			}
		}
		System.out.println(haikuLine2);
		
	//----------------------------------------------------------------------------------------------	
		currentSybCounter = 0;
		currentSybSelection = 0;
		for(int i = 0; i < lineTres; i++)
		{
			currentSybSelection = rGenerator.nextInt(lineTres);
			if(currentSybCounter == 4)
			{
				currentSybCounter = currentSybCounter + 1;
				haikuLine3.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
			}	
			if(currentSybCounter + currentSybSelection <= lineTres)
			{
				if(currentSybSelection == oneSyllable)
				{
				currentSybCounter = currentSybCounter + 1;
				haikuLine3.add(oneSyllableWords[rGenerator.nextInt(oneSyllableWords.length)]);
				}
				if(currentSybSelection == twoSyllables)
				{
				currentSybCounter = currentSybCounter +2;
				haikuLine3.add(twoSyb[rGenerator.nextInt(twoSyb.length)]);	
				}	
				if(currentSybSelection == threeSyllables)
				{
				currentSybCounter = currentSybCounter + 3;
				haikuLine3.add(threeSyb[rGenerator.nextInt(threeSyb.length)]);		
				}	
				if(currentSybSelection == fourSyllables)
				{
				currentSybCounter = currentSybCounter + 4;
				haikuLine3.add(fourSyb[rGenerator.nextInt(fourSyb.length)]);	
				}	
			} else {
			   i--;
			}
		}
		System.out.println(haikuLine3);
		
		
	}//end main
}//end class
