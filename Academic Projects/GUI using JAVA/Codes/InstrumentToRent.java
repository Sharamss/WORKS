/**
 * Write a description of class InstrumentToRent here.
 *
 * @author (Sharams Kunwar)
 * @version ()
 */
public class InstrumentToRent extends Instrument
{
    /*creating variables*/
    private int ChargePerDay;
    private String DateOfRent;
    private String DateOfReturn;
    private int NoofDays;
    private boolean IsRented;
    
    //constructor for InstrumentToRent
    
    public InstrumentToRent(String Instrument_Name,int ChargePerDay)
    {
        super(Instrument_Name);
        this.ChargePerDay =ChargePerDay;
        this.DateOfRent ="";
        this.DateOfReturn = "";
        this.NoofDays =0;
        this.IsRented =false;
    }
    
    //accessor method for all the attributes;
    public int getChargePerDay()
    {
        return this.ChargePerDay;
    }
    public String getDateOfRent()
    {
        return this.DateOfRent;
    }
    public String getDateOfReturn()
    {
        return this.DateOfReturn;
    }
    public int getNoofDays()
    {
        return this.NoofDays;
    }
    public boolean getIsRented()
    {
        return this.IsRented;
    }
    
    //mutator for all the attributes;
    public void setChargePerDay(int ChargePerDay)
    {
        this.ChargePerDay = ChargePerDay;
    }
    public void setDateOfRent(String DateOfRent)
    {
        this.DateOfRent = DateOfRent;
    }
    public void setDateOfReturn(String DateOfReturn)
    {
        this.DateOfReturn = DateOfReturn;
    }
    public void setNoofDays(int noOfDays)
    {
        this.NoofDays = NoofDays;
    }
    public void setIsRented(boolean IsRented)
    {
        this.IsRented = IsRented;
    }
    
    public void Rent(String Name, String Phone, int Pan_Number, String DateOfRent, String DateOfReturn, int NoofDays)
    {
        if(IsRented ==true)
        {
            System.out.println("No instrument is available.");
        }
        else
        {
            super.setCustomer_Name(Name);
            super.setCustomer_Mobile_Number(Phone);
            super.setPan_Number(Pan_Number);
            this.DateOfRent = DateOfRent;
            this.DateOfReturn = DateOfReturn;
            this.NoofDays = NoofDays;
            IsRented =true;
            int TotalCharge;
            TotalCharge = NoofDays * this.ChargePerDay;
            System.out.println("Name of the Customer is " + Name);
            System.out.println("Mobile Number of Customer is " +Phone);
            System.out.println("Pan_Number is " + Pan_Number);
            System.out.println("DateOfRent is " + DateOfRent);
            System.out.println("DateOfReturn is " + DateOfReturn);
            System.out.println("NoofDays is " + NoofDays);
            System.out.println("The Total Charge is " + TotalCharge);
            
        } 
    }
    public void returnInstrument()
   {
       if(IsRented == false)
       {
           System.out.println("The Instrument Has Not Been Rented");
       }
       else
       {
           this.setCustomer_Name("");
           this.setCustomer_Mobile_Number("");
           this.setDateOfReturn("");
           this.setDateOfRent("");
           this.setNoofDays(0);
           this.setPan_Number(0);
           this.setIsRented(false);
       }
   }
    public void Return()
    {
        if(IsRented ==false)
        {
            System.out.print("The instrument has not been rented");
        }
        else
        {
            super.display();
            this.setCustomer_Name("");
            this.setCustomer_Mobile_Number("");
            this.setDateOfReturn("");
            this.setDateOfRent("");
            this.setNoofDays(0);
            this.setPan_Number(0);
            this.setIsRented(false);
            
        }
    }
    public void display()
    {   
        super.display();
        if(IsRented ==true)
        {
            System.out.println("customer's name: "+getCustomer_Name() );
            System.out.println("DateOfRent: " + DateOfRent);
            System.out.println("DateOfReturn: " + DateOfReturn);
            System.out.println("Pan Number: "+getPan_Number());
            System.out.println("Phone Number: "+ getCustomer_Mobile_Number());
        }
    }
}