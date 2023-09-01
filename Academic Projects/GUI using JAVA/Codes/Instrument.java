/**
 * Write a description of class Instrument here.
 *
 * @author (Sharams Kunwar)
 * @version ()
 */
public class Instrument
{       
    private static int Instrument_ID;
    private String Instrument_Name;
    private String Customer_Name;
    private String Customer_Mobile_Number;
    private int Pan_Number;
    
    //constructor;
    public Instrument(String Instrument_Name)
    {
        this.Instrument_Name = Instrument_Name;
        Instrument_ID ++;
        this.Customer_Name ="";
        this.Customer_Mobile_Number ="";
        this.Pan_Number = 0;
        
    }
    
    
    //Accessor method to all the attributes;
    public int getInstrument_ID()
    {
        return Instrument_ID;
    }
    public String getInstrument_Name()
    {
        return this.Instrument_Name;
    }
    public String getCustomer_Name()
    {
        return this.Customer_Name;
    }
    public String getCustomer_Mobile_Number()
    {
        return this.Customer_Mobile_Number;
    }
    public int getPan_Number()
    {
        return this.Pan_Number;
    }


    //mutator method for the attributes;
    public void setInstrument_ID(int Instrument_ID)
    {
        Instrument.Instrument_ID = Instrument_ID;
    }
    public void setInstrument_Name(String Instrument_Name)
    {
        this.Instrument_Name = Instrument_Name;
    }
    public void setCustomer_Name(String Customer_Name)
    {
        this.Customer_Name = Customer_Name;
    }
    public void setCustomer_Mobile_Number(String Customer_Mobile_Number)
    {
        this.Customer_Mobile_Number =Customer_Mobile_Number;
    }
    public void setPan_Number(int Pan_Number)
    {
        this.Pan_Number =Pan_Number;
    }
    
    //method    
    public void display()
    {
        System.out.println("Instrument ID: " + Instrument_ID);
        System.out.println("Instrument Name: "+ Instrument_Name);
        
        if(Customer_Name !=""&& Customer_Mobile_Number!=""&& Pan_Number!=0)
        {
            System.out.println("Customer_Name:" + Customer_Name);
            System.out.println("Customer_Mobile_Number:" + Customer_Mobile_Number);
            System.out.println("Pan_Number:" + Pan_Number);
        }
    }
}