class Solution {
    public boolean isValid(String word) {
        int vc=0, cc=0;
        if (word.length()<3)
        return false;
        else
        {
            for (int i=0; i<word.length(); i++)
            {
                char ch= word.charAt(i);
                if (Character.isDigit(ch) || Character.isLetter(ch))
                {
                    if (Character.isLetter(ch))
                    {
                        if (ch== 'A' || ch=='a'||ch== 'E' || ch== 'e'|| ch== 'I' || ch== 'i' ||ch=='O' || ch== 'o'|| ch== 'U' || ch=='u')
                        vc++;
                        else
                        cc++;
                    }
                }
                else
                return false;
            }
            if(vc<1 || cc<1)
            return false;
            else 
            return true;
        }
    }
}