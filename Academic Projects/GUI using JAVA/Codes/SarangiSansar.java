
/**
 * Write a description of class SarangiSansar here.
 *
 * @author (Sharams Kunwar)
 * @version (a version number or a date)
 */
import javax.swing.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.color.*;

public class SarangiSansar implements ActionListener
{
    private JFrame myFrame;
    private JPanel aPanel, rPanel, sPanel;
    private JLabel TitleLB, NameCustomerLB, PhoneNumLB, panLB, ins_to_rentLB, 
    ins_to_sellLB,NameINSrentLB, NumofDaysLB, ChargeperDayLB, RentDateLB, 
    ReturnDateLB, NameINSsellLB, PriceLB, DiscountLB, SellDateLB;

    private JTextField NameCustomerTF, PhoneNumTF, panTF, NameINSrentTF, 
    NameINSsellTF, NumofDaysTF, PriceTF, ChargeperDayTF, DiscountTF;

    private JComboBox RentDateCBy, ReturnDateCBy, SellDateCBy;
    private JComboBox RentDateCBm, ReturnDateCBm, SellDateCBm;
    private JComboBox RentDateCBd, ReturnDateCBd, SellDateCBd;

    private JButton RentINSbtn, ReturnINSbtn, AddRentbtn, DisplayRentbtn, ClearRentbtn,
    SellINSbtn, AddSellbtn, DisplaySellbtn, ClearSellbtn;

    ArrayList<Instrument> instruments = new ArrayList<Instrument>();
    public SarangiSansar(){
        //Main Frame
        myFrame = new JFrame("Sarangi Sansar");

        //Creating
        //Panels
        aPanel = new JPanel();
        rPanel = new JPanel();
        sPanel = new JPanel();

        //labels

        //FrameLabels
        TitleLB = new JLabel("Welcome to Sarangi Sansar!", SwingConstants.CENTER);
        NameCustomerLB = new JLabel("Customer Name:");
        PhoneNumLB = new JLabel("Phone Number:");
        panLB = new JLabel("Customer PAN:");

        //RentPanelLabels
        ins_to_rentLB = new JLabel("Instrument to Rent", SwingConstants.CENTER);
        NameINSrentLB = new JLabel("Instrument Name:");
        NumofDaysLB = new JLabel("Number of Days:");
        ChargeperDayLB = new JLabel("Charge Per Day:");
        RentDateLB = new JLabel("Rent Date:");
        ReturnDateLB = new JLabel("Return Date:");

        //SellPanelLables
        ins_to_sellLB = new JLabel("Instrument to Sell", SwingConstants.CENTER);
        NameINSsellLB = new JLabel("Instrument Name:");
        PriceLB = new JLabel("Price:");
        DiscountLB = new JLabel("Discount Percent:");
        SellDateLB = new JLabel("Selling Date:");

        //TextFields
        //FrameTextFields
        NameCustomerTF = new JTextField();
        PhoneNumTF = new JTextField();
        panTF = new JTextField();

        //RentPanel TextFields
        NameINSsellTF = new JTextField();
        NumofDaysTF = new JTextField();
        ChargeperDayTF = new JTextField();

        //SellPanel TesxtFields
        NameINSrentTF = new JTextField();
        PriceTF = new JTextField();
        DiscountTF = new JTextField();

        //ComboBox
        //array
        String y[]={"Year","2017","2018","2019","2020","2021","2022"};
        String m[]={"Month","January","February","March","April","May","June", "July"
            , "August", "September", "October", "November", "December"};
        String d[]={"Day","1","2","3","4","5","6","7","8","9","10","11","12","13",
                "14","15","16","17","18","19","20","21","22","23","24",
                "25","26","27","28","29","30","31"};

        //Rent ComboBox
        RentDateCBy = new JComboBox(y);
        RentDateCBm = new JComboBox(m);
        RentDateCBd = new JComboBox(d);

        //Return ComboBox
        ReturnDateCBy = new JComboBox(y);
        ReturnDateCBm = new JComboBox(m);
        ReturnDateCBd = new JComboBox(d);

        //Sell ComboBox
        SellDateCBy = new JComboBox(y);
        SellDateCBm = new JComboBox(m);
        SellDateCBd = new JComboBox(d);

        //Buttons

        //RentPanel Buttons
        RentINSbtn = new JButton("Rent the Instrument");
        ReturnINSbtn = new JButton("Return the Instrument");
        AddRentbtn = new JButton("Add the Instrument To Rent");
        DisplayRentbtn = new JButton("Display");
        ClearRentbtn = new JButton("Clear");

        //SellPanel Buttons
        SellINSbtn = new JButton("Sell the Instrument");
        AddSellbtn = new JButton("Add the Instrument To Sell");
        DisplaySellbtn = new JButton("Display");
        ClearSellbtn = new JButton("Clear");

        //Setting Bounds

        //main frame
        myFrame.getRootPane().setBorder(BorderFactory.createLineBorder(Color.black));

        //aPanel
        aPanel.setBounds(0, 0, 800, 147);
        aPanel.setBackground(new Color(243,237,210));
        aPanel.setBorder(BorderFactory.createLineBorder(Color.black));

        //1.Title
        TitleLB.setBounds(290, 20, 220, 30);
        TitleLB.setForeground(Color.WHITE);
        TitleLB.setBackground(Color.BLACK);
        TitleLB.setFont(new Font("Helvetica", Font.PLAIN, 14));
        TitleLB.setOpaque(true);

        //2.Customer Name
        //Label
        NameCustomerLB.setBounds(23,94,110,20);
        NameCustomerLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //TextField
        NameCustomerTF.setBounds(138, 94, 145, 29);

        //3.Phone Number
        //Label
        PhoneNumLB.setBounds(317, 94, 110, 20);
        PhoneNumLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //TextField
        PhoneNumTF.setBounds(426, 94, 138,29);

        //4.PAN no
        //label
        panLB.setBounds(594, 94, 130, 20);
        panLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //textfield
        panTF.setBounds(700, 94, 75, 29);

        //end of aPanel

        //rPanel
        rPanel.setBounds(0,147,400,545);
        rPanel.setBackground(new Color(238,238,238));
        rPanel.setBorder(BorderFactory.createLineBorder(Color.gray));

        //1.Title
        ins_to_rentLB.setBounds(104, 49, 192, 30);
        ins_to_rentLB.setForeground(Color.WHITE);
        ins_to_rentLB.setBackground(Color.BLACK);
        ins_to_rentLB.setFont(new Font("Helvetica", Font.PLAIN, 14));
        ins_to_rentLB.setOpaque(true);

        //2.Labels
        //ins Name
        NameINSrentLB.setBounds(23, 104, 115, 20);
        NameINSrentLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //numofdays
        NumofDaysLB.setBounds(23, 159, 110, 20);
        NumofDaysLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //chargeperday
        ChargeperDayLB.setBounds(23, 204, 110, 20);
        ChargeperDayLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //rentdate
        RentDateLB.setBounds(23, 249, 110, 20);
        RentDateLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //returndate
        ReturnDateLB.setBounds(23, 294, 110, 20);
        ReturnDateLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //3.textfields
        //ins name
        NameINSrentTF.setBounds(164, 104, 198, 29);

        //numofdays
        NumofDaysTF.setBounds(164, 159, 198, 29);

        //chargeperday
        ChargeperDayTF.setBounds(164, 204, 198, 29);

        //4. buttons
        //rentinstrumentbtn
        RentINSbtn.setBounds(23,364,170,40);
        RentINSbtn.setForeground(Color.BLACK);
        RentINSbtn.setBackground(Color.WHITE);
        RentINSbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        RentINSbtn.setOpaque(true);

        //returninsbtn
        ReturnINSbtn.setBounds(201,364,175,40);
        ReturnINSbtn.setForeground(Color.BLACK);
        ReturnINSbtn.setBackground(Color.WHITE);
        ReturnINSbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        ReturnINSbtn.setOpaque(true);

        //addtorentbtn
        AddRentbtn.setBounds(23,429,353,40);
        AddRentbtn.setForeground(Color.BLACK);
        AddRentbtn.setBackground(Color.WHITE);
        AddRentbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        AddRentbtn.setOpaque(true);

        //displaybtn
        DisplayRentbtn.setBounds(23,494,150,40);
        DisplayRentbtn.setForeground(Color.BLACK);
        DisplayRentbtn.setBackground(Color.WHITE);
        DisplayRentbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        DisplayRentbtn.setOpaque(true);

        //clearbtn
        ClearRentbtn.setBounds(226,494,150,40);
        ClearRentbtn.setForeground(Color.BLACK);
        ClearRentbtn.setBackground(Color.WHITE);
        ClearRentbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        ClearRentbtn.setOpaque(true);

        //5. Combobox
        //rentdate
        RentDateCBy.setBounds(157, 244, 65, 32);
        RentDateCBm.setBounds(232, 244, 65, 32);
        RentDateCBd.setBounds(307, 244, 65, 32);

        //returndate
        ReturnDateCBy.setBounds(157, 291, 65, 32);
        ReturnDateCBm.setBounds(232, 291, 65, 32);
        ReturnDateCBd.setBounds(307, 291, 65, 32);

        //array

        //end of rPanel
        //sPanel
        sPanel.setBounds(400,147,400,545);
        sPanel.setBackground(new Color(238,238,238));
        sPanel.setBorder(BorderFactory.createLineBorder(Color.gray));

        //1.Title
        ins_to_sellLB.setBounds(104, 49, 192, 30);
        ins_to_sellLB.setForeground(Color.WHITE);
        ins_to_sellLB.setBackground(Color.BLACK);
        ins_to_sellLB.setFont(new Font("Helvetica", Font.PLAIN, 14));
        ins_to_sellLB.setOpaque(true);

        //2.labels
        //insname
        NameINSsellLB.setBounds(23, 104, 115, 20);
        NameINSsellLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //price
        PriceLB.setBounds(23, 159, 110, 20);
        PriceLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //discount
        DiscountLB.setBounds(23, 204, 115, 20);
        DiscountLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //sellingdate
        SellDateLB.setBounds(23, 249, 110, 20);
        SellDateLB.setFont(new Font("Helvetica", Font.PLAIN, 14));

        //3.textfields
        //insname
        NameINSsellTF.setBounds(164, 104, 198, 29);

        //Price
        PriceTF.setBounds(164, 159, 198, 29);

        //Discount
        DiscountTF.setBounds(164, 204, 198, 29);

        //4.buttons
        //sellbtn
        SellINSbtn.setBounds(115,364,178,40);
        SellINSbtn.setForeground(Color.BLACK);
        SellINSbtn.setBackground(Color.WHITE);
        SellINSbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        SellINSbtn.setOpaque(true);

        //addtosellbtn
        AddSellbtn.setBounds(23,429,353,40);
        AddSellbtn.setForeground(Color.BLACK);
        AddSellbtn.setBackground(Color.WHITE);
        AddSellbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        AddSellbtn.setOpaque(true);

        //displaybtn
        DisplaySellbtn.setBounds(23,494,150,40);
        DisplaySellbtn.setForeground(Color.BLACK);
        DisplaySellbtn.setBackground(Color.WHITE);
        DisplaySellbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        DisplaySellbtn.setOpaque(true);

        //clearbtn
        ClearSellbtn.setBounds(226,494,150,40);
        ClearSellbtn.setForeground(Color.BLACK);
        ClearSellbtn.setBackground(Color.WHITE);
        ClearSellbtn.setFont(new Font("Helvetica", Font.PLAIN, 14));
        ClearSellbtn.setOpaque(true);

        //combobox
        SellDateCBy.setBounds(157, 244, 65, 32);
        SellDateCBm.setBounds(232, 244, 65, 32);
        SellDateCBd.setBounds(307, 244, 65, 32);

        
        //Adding to Frame
        //Panels
        myFrame.add(aPanel);
        myFrame.add(rPanel);
        myFrame.add(sPanel);

        //components of aPanel
        //1. Labels
        aPanel.add(TitleLB);
        aPanel.add(NameCustomerLB);
        aPanel.add(PhoneNumLB);
        aPanel.add(panLB);

        //2.TextFields
        aPanel.add(NameCustomerTF);
        aPanel.add(PhoneNumTF);
        aPanel.add(panTF);

        //components of Rent Panel
        //1.Labels
        rPanel.add(ins_to_rentLB);
        rPanel.add(NameINSrentLB);
        rPanel.add(NumofDaysLB);
        rPanel.add(ChargeperDayLB);
        rPanel.add(RentDateLB);
        rPanel.add(ReturnDateLB);

        //2.TextFields
        rPanel.add(NameINSrentTF);
        rPanel.add(NumofDaysTF);
        rPanel.add(ChargeperDayTF);

        //3.ComboBox
        rPanel.add(RentDateCBy);
        rPanel.add(RentDateCBm);
        rPanel.add(RentDateCBd);
        rPanel.add(ReturnDateCBy);
        rPanel.add(ReturnDateCBm);
        rPanel.add(ReturnDateCBd);

        //4.Buttons
        rPanel.add(RentINSbtn);
        rPanel.add(ReturnINSbtn);
        rPanel.add(AddRentbtn);
        rPanel.add(DisplayRentbtn);
        rPanel.add(ClearRentbtn);

        //components of sell panel
        //1.Labels
        sPanel.add(ins_to_sellLB);
        sPanel.add(NameINSsellLB);
        sPanel.add(PriceLB);
        sPanel.add(DiscountLB);
        sPanel.add(SellDateLB);

        //2.Textfields
        sPanel.add(NameINSsellTF);
        sPanel.add(PriceTF);
        sPanel.add(DiscountTF);   

        //3.ComboBox
        sPanel.add(SellDateCBy);
        sPanel.add(SellDateCBm);
        sPanel.add(SellDateCBd);

        //4.Buttons
        sPanel.add(SellINSbtn);
        sPanel.add(AddSellbtn);
        sPanel.add(DisplaySellbtn);
        sPanel.add(ClearSellbtn);

        //ActionListener
        SellINSbtn.addActionListener(this);
        AddSellbtn.addActionListener(this);
        DisplaySellbtn.addActionListener(this);
        ClearSellbtn.addActionListener(this);
        RentINSbtn.addActionListener(this);
        ReturnINSbtn.addActionListener(this);
        AddRentbtn.addActionListener(this);
        DisplayRentbtn.addActionListener(this);
        ClearRentbtn.addActionListener(this);

        //setting
        myFrame.setSize(817,732);
        myFrame.setLayout(null);
        aPanel.setLayout(null);
        rPanel.setLayout(null);
        sPanel.setLayout(null);

        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        myFrame.setVisible(true);

    }

    public static void main(String[]args)
    {
        SarangiSansar obj = new SarangiSansar();

    }

    //Add Instrument for Rent Button
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == AddRentbtn){
            if(NameINSrentTF.getText().isEmpty() || ChargeperDayTF.getText().isEmpty())
            {
                JOptionPane.showMessageDialog(myFrame, "Name of the Instrument and Charge Per Day is Mandatory to Be Filled.");

            }
            else{
                try{
                    String INSname = NameINSrentTF.getText();
                    String ChargePday = ChargeperDayTF.getText();
                    int Charge = Integer.parseInt(ChargePday);
                    boolean isAvailable = false;

                    if(instruments.isEmpty()){
                        InstrumentToRent INSrent = new InstrumentToRent(INSname, Charge);
                        if(INSrent instanceof InstrumentToRent){
                            instruments.add(INSrent);

                            JOptionPane.showMessageDialog(myFrame, "Instrument has been Added Successfully.");
                        }
                    }
                    else{
                        for(Instrument instrument: instruments){
                            if(instrument instanceof InstrumentToRent){
                                if(instrument.getInstrument_Name().equals(INSname)){
                                    isAvailable= true;
                                }
                            }
                        }
                        if(isAvailable == true){
                            JOptionPane.showMessageDialog(myFrame, "Instrument is Already Available.");
                        }
                        else{
                            InstrumentToRent INSrent = new InstrumentToRent(INSname, Charge);
                            if(INSrent instanceof InstrumentToRent){
                                instruments.add(INSrent);

                                JOptionPane.showMessageDialog(myFrame, "Instrument has been Added Successfully.");
                            }
                        }
                    }
                }
                catch(NumberFormatException except){
                    JOptionPane.showMessageDialog(rPanel, "Invalid Data Entered","Error", JOptionPane.ERROR_MESSAGE);

                }
            }
        }

        //Add Instrument for Sell Button
        if(e.getSource() == AddSellbtn){
            if(NameINSsellTF.getText().isEmpty() || PriceTF.getText().isEmpty())
            {
                JOptionPane.showMessageDialog(myFrame, "Name of the Instrument and Price is Mandatory to Be Filled.");

            }
            else{
                try{
                    String INSname = NameINSsellTF.getText();
                    String Prices = PriceTF.getText();
                    float pr = Float.parseFloat(Prices);
                    boolean isAvailable = false;

                    if(instruments.isEmpty()){
                        InstrumentToSell INSsell = new InstrumentToSell(pr,INSname);
                        if(INSsell instanceof InstrumentToSell){
                            instruments.add(INSsell);

                            JOptionPane.showMessageDialog(myFrame, "Instrument has been Added Successfully.");
                        }
                    }
                    else{
                        for(Instrument instrument: instruments){
                            if(instrument instanceof InstrumentToSell){
                                if(instrument.getInstrument_Name().equals(INSname)){
                                    isAvailable= true;
                                }
                            }
                        }
                        if(isAvailable == true){
                            JOptionPane.showMessageDialog(myFrame, "Instrument is Already Available.");
                        }
                        else{
                            InstrumentToSell INSsell = new InstrumentToSell(pr, INSname);
                            if(INSsell instanceof InstrumentToSell){
                                instruments.add(INSsell);

                                JOptionPane.showMessageDialog(myFrame, "Instrument has been Added Successfully.");
                            }
                        }
                    }
                }
                catch(NumberFormatException except){
                    JOptionPane.showMessageDialog(myFrame, "Invalid Data Entered","Error", JOptionPane.ERROR_MESSAGE);

                }
            }
        }

        //Rent the instrument button
        if(e.getSource()==RentINSbtn){
            if(NameCustomerTF.getText().isEmpty() || PhoneNumTF.getText().isEmpty() || panTF.getText().isEmpty() || NameINSrentTF.getText().isEmpty()
            || ChargeperDayTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "Please, Fill up all the Details");

            }
            else{
                try{
                    String CName = NameCustomerTF.getText();
                    String PNum = PhoneNumTF.getText();
                    String panNo = panTF.getText();
                    String INSname = NameINSrentTF.getText();
                    String ChargePday = ChargeperDayTF.getText();
                    String DaysNo = NumofDaysTF.getText();
                    String DateReturn = ReturnDateCBy.getSelectedItem().toString() + ReturnDateCBm.getSelectedItem().toString() + ReturnDateCBd.getSelectedItem().toString();
                    String DateRent = RentDateCBy.getSelectedItem().toString() + RentDateCBm.getSelectedItem().toString() + RentDateCBd.getSelectedItem().toString();
                    int PAN = Integer.parseInt(panNo);
                    int Charge = Integer.parseInt(ChargePday);
                    int NOdays = Integer.parseInt(DaysNo);

                    if(instruments.isEmpty()){
                        JOptionPane.showMessageDialog(myFrame, "Instrument hasn't been Added For Rent");
                    }
                    else{
                        for(Instrument instrument: instruments){
                            if(instrument instanceof InstrumentToRent){
                                InstrumentToRent rent = (InstrumentToRent)instrument;
                                if(rent.getInstrument_Name().equals(INSname)){

                                    if(rent.getIsRented()==true){
                                        JOptionPane.showMessageDialog(myFrame, "The Instrument has been Already Rented");
                                        rent.Rent(CName,PNum, PAN, DateRent, DateReturn, NOdays);
                                    }
                                    else{
                                        JOptionPane.showMessageDialog(myFrame, "The Instrument has been Rented");
                                        rent.Rent(CName,PNum, PAN, DateRent, DateReturn, NOdays);
                                        rent.setIsRented(true);
                                    }
                                }
                            }
                        }
                    }
                }
                catch(NumberFormatException except){
                    JOptionPane.showMessageDialog(myFrame, "Invalid Data Entered","Error", JOptionPane.ERROR_MESSAGE);

                }
            }
        }

        //Sell the Instrument Button
        if(e.getSource()==SellINSbtn){
            if(NameCustomerTF.getText().isEmpty() || PhoneNumTF.getText().isEmpty() || panTF.getText().isEmpty() || NameINSsellTF.getText().isEmpty()
            || PriceTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "Please, Fill up all the Details");

            }
            else{
                try{
                    String CName = NameCustomerTF.getText();
                    String PNum = PhoneNumTF.getText();
                    String panNo = panTF.getText();
                    String INSname = NameINSsellTF.getText();
                    String Discount = DiscountTF.getText();
                    String Price = PriceTF.getText();
                    String DateSell = SellDateCBy.getSelectedItem().toString() + SellDateCBm.getSelectedItem().toString() + SellDateCBd.getSelectedItem().toString();
                    int PAN = Integer.parseInt(panNo);
                    float Disc = Float.parseFloat(Discount);
                    float Pr = Float.parseFloat(Price);

                    if(instruments.isEmpty()){
                        JOptionPane.showMessageDialog(myFrame, "Instrument hasn't been Added For Sell");
                    }
                    else{
                        for(Instrument instrument: instruments){
                            if(instrument instanceof InstrumentToSell){
                                InstrumentToSell Sells = (InstrumentToSell)instrument;
                                if(Sells.getInstrument_Name().equals(INSname)){

                                    if(Sells.getisSold()==true){
                                        JOptionPane.showMessageDialog(myFrame, "The Instrument has been Already Sold");
                                        Sells.sell(CName,PNum, PAN, DateSell, Disc);
                                    }
                                    else{
                                        JOptionPane.showMessageDialog(myFrame, "The Instrument has been Sold");
                                        Sells.sell(CName,PNum, PAN, DateSell, Disc);
                                        Sells.setisSold(true);
                                    }
                                }
                            }
                        }
                    }
                }
                catch(NumberFormatException except){
                    JOptionPane.showMessageDialog(myFrame, "Invalid Data Entered","Error", JOptionPane.ERROR_MESSAGE);

                }
            }
        }

        //Return the Instrument Button
        if(e.getSource()==ReturnINSbtn){
            if( NameINSrentTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "Please, Fill up the 'Instrument Name'");
            }
            else{
                String INSname = NameINSrentTF.getText();
                if(instruments.isEmpty()){
                    JOptionPane.showMessageDialog(myFrame, "Instrument hasn't been Rented.");
                }
                else{
                    for(Instrument instrument : instruments){
                        if(instrument instanceof InstrumentToRent){
                            if(instrument.getInstrument_Name().equals(INSname)){
                                InstrumentToRent rent = (InstrumentToRent)instrument;
                                if(rent.getIsRented()==true){
                                    JOptionPane.showMessageDialog(myFrame, "The Instrument Has Been Returned.");
                                    rent.setIsRented(false);
                                }
                                else{
                                    JOptionPane.showMessageDialog(myFrame, "Instrument Hasn't Been Rented. ");   
                                }
                            }
                        }
                    }
                }
            }
        }

        //Display Rent Button
        if(e.getSource()== DisplayRentbtn){
            if(NameCustomerTF.getText().isEmpty() && PhoneNumTF.getText().isEmpty() && panTF.getText().isEmpty() && NameINSrentTF.getText().isEmpty()
            && ChargeperDayTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "NOTHING TO DISPLAY!! :(");
            }else{  
                for(Instrument inst : instruments){
                    if(inst instanceof InstrumentToRent){
                        InstrumentToRent rents = (InstrumentToRent)inst;
                        rents.display();
                    }
                }
            }
        }

        //Display Sell Button
        if(e.getSource()== DisplaySellbtn){
            if(NameCustomerTF.getText().isEmpty() && PhoneNumTF.getText().isEmpty() && panTF.getText().isEmpty() && NameINSsellTF.getText().isEmpty()
            && PriceTF.getText().isEmpty() && DiscountTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "NOTHING TO DISPLAY!! :(");
            }else{  
                for(Instrument inst : instruments){
                    if(inst instanceof InstrumentToSell){
                        InstrumentToSell sells = (InstrumentToSell)inst;
                        sells.display();
                    }
                }
            }
        }

        //Clear Rent Button
        if(e.getSource()== ClearRentbtn){
            if(NameCustomerTF.getText().isEmpty() && PhoneNumTF.getText().isEmpty() && panTF.getText().isEmpty() && NameINSrentTF.getText().isEmpty()
            && ChargeperDayTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "NOTHING TO CLEAR!! :(");
            }else{
                NameCustomerTF.setText("");
                PhoneNumTF.setText("");
                panTF.setText("");
                NameINSrentTF.setText("");
                ChargeperDayTF.setText("");
                NumofDaysTF.setText("");
                RentDateCBy.setSelectedItem("Year");
                RentDateCBm.setSelectedItem("Month");
                RentDateCBd.setSelectedItem("Day");
                ReturnDateCBy.setSelectedItem("Year");
                ReturnDateCBm.setSelectedItem("Month");
                ReturnDateCBd.setSelectedItem("Day");
                JOptionPane.showMessageDialog(myFrame, "Successfully cleared!! :)");
            }
        }

        //Clear Sell Button
        if(e.getSource()== ClearSellbtn){
            if(NameCustomerTF.getText().isEmpty() && PhoneNumTF.getText().isEmpty() && panTF.getText().isEmpty() && NameINSsellTF.getText().isEmpty()
            && PriceTF.getText().isEmpty() && DiscountTF.getText().isEmpty()){
                JOptionPane.showMessageDialog(myFrame, "NOTHING TO CLEAR!! :(");

            }else{
                NameCustomerTF.setText("");
                PhoneNumTF.setText("");
                panTF.setText("");
                NameINSsellTF.setText("");
                PriceTF.setText("");
                DiscountTF.setText("");
                SellDateCBy.setSelectedItem("Year");
                SellDateCBm.setSelectedItem("Month");
                SellDateCBd.setSelectedItem("Day");
                JOptionPane.showMessageDialog(myFrame, "Successfully cleared!! :)");
            } 
        }
    }
}

