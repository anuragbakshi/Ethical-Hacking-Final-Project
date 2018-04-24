//Tuan Le

package email;

import java.util.*;
import javax.mail.Authenticator;
import javax.mail.Message;
import javax.mail.MessagingException;
import javax.mail.Session;
import javax.mail.Transport;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;
import javax.mail.PasswordAuthentication;
import static java.lang.System.*;

import java.io.File;
import java.io.FileNotFoundException;

public class SpoofEmail 
{
	public static void main(String [] args)
	{
		/* CS 378 EH Modifications */
		//Variables
		String to, from, subject, body, host, port, user, pass, dir, siteip;
		ArrayList<String> emailList = new ArrayList<String>();
		
		//Collect user input
		Scanner keyboard = new Scanner(System.in);
		out.println("Enter the email list path (include the file): ");
		dir = keyboard.nextLine();
		out.println("Enter the ip of the cloned site: ");
		siteip = keyboard.nextLine();
		keyboard.close();
		
		//Parse through email list
		try
		{
			Scanner el = new Scanner(new File(dir));
			while(el.hasNext())
			{
				emailList.add(el.next());
			}
			el.close();
		}
		catch (FileNotFoundException e)
		{
			e.printStackTrace();
		}
		
		/* CHANGE HARDCODED VARIABLES TO MATCH PRESENTATION MACHINE'S */
		
		//From address
		from = "notification@facebookemail.com";
		//Subject line
		subject = "Your friends have invited you to join a group!";
		//Body
		body = "Click <a href='http://" + siteip + "'>here</a> to resolve all pending invitations.";
		
		//SMTP credentials
		host = "localhost";
		port = "25";
		user = "test@test.com";
		pass = "test";
		
		//SMTP server information
		Properties prop = new Properties();
		prop.put("mail.smtp.host", host);
		prop.put("mail.smtp.starttls.enable", "true");
		prop.put("mail.smtp.port", port);
		prop.put("mail.smtp.auth", "true");
		
		//Authentication Information
		Authenticator auth = new Authenticator() 
		{
			protected PasswordAuthentication getPasswordAuthentication()
			{
				return new PasswordAuthentication(user, pass);
			}
		};
		Session sesobj = Session.getInstance(prop, auth);
		
		//If the email list isn't empty, iterate through it
		if(!emailList.isEmpty())
		{
			for(int i = 0; i < emailList.size(); i++)
			{
				//Current entry in list of emails
				to = emailList.get(i);
				
				//Try to send message
				try
				{
					MimeMessage msgobj = new MimeMessage(sesobj);
					msgobj.setFrom(new InternetAddress(from));
					msgobj.setRecipients(Message.RecipientType.TO, InternetAddress.parse(to));
					msgobj.setSubject(subject);
					msgobj.setText(body, "utf-8", "html");
					Transport.send(msgobj);
					out.println("Email successfully sent to " + to);
				}
				catch(MessagingException exp)
				{
					exp.printStackTrace();
					throw new RuntimeException(exp);
				}
			}
		}
	}
}