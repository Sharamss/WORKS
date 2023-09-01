/**
 * Write a description of class InstrumentToSell here.
 *
 * @author (Sharams Kunwar)
 * @version ()
 */
public class InstrumentToSell extends Instrument
{   
    private float Price;
    private String SellDate;
    private float DiscountPercent;
    private boolean isSold;
    
    
    //constructor
    
    public InstrumentToSell(float Price, String Name)
    {
        super(Name);
        this.Price = Price;
        this.SellDate ="";
        this.DiscountPercent =0.0f;
        this.isSold =false;
    }
    
    //accessor method for the attributes;
    public float getPrice()
    {
        return this.Price;
    }
    public String getSellDate()
    {
        return this.SellDate;
    }
    public float getDiscountPercent()
    {
        return this.DiscountPercent;
    }
    public boolean getisSold()
    {
        return this.isSold;
    }
    
    //mutator method for the attributes;
    public void setPrice(float Price)
    {   if(this.isSold ==false)
        {
            this.Price = Price;
        }
        else
        {
            System.out.println("The Instrument Has Been Already Sold");
        }
    }
    public void setSellDate(String SellDate)
    {
        this.SellDate = SellDate;
    }
    public void setDiscountPercent(float DiscountPercent)
    {
        this.DiscountPercent = DiscountPercent;
    }
    public void setisSold(boolean isSold)
    {
        this.isSold = isSold;
    }
    public void sell(String Customer_Name, String Phone, int Pan_Number, String SellDate, float DiscountPercent)
    {
        if(this.isSold==true)
        {
            System.out.println("The Instrument Has Been Sold.");
            System.out.println("Customer Name: " +Customer_Name);
            System.out.println("Customer Mobile Number: " + Phone);
            System.out.println("Customer Pan Number: "+ Pan_Number);
        }
        else
        {
            this.SellDate =SellDate;
            this.DiscountPercent=DiscountPercent;
            isSold =true;
            super.setCustomer_Name(Customer_Name);
            super.setCustomer_Mobile_Number(Phone);
            super.setPan_Number(Pan_Number);
            Price =Price -((DiscountPercent/100) * Price);
        }
    }
    public void display()
    {
        super.display();
        System.out.println("The Price of The Instrument is: " +Price);
        if(isSold == true)
        {
            System.out.println("Name of Customer: " +getCustomer_Name());
            System.out.println("Phone Number of the Customer: "+ getCustomer_Mobile_Number());
            System.out.println("Pan Number of the Customer: "+ getPan_Number());
            System.out.println("Sold Date: "+SellDate);
        }
        
    }
}