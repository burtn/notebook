<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">


<xsl:template match="keywords">
  <html>
		<head>		
			<title><xsl:value-of select="@set" /></title>	
                         <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"
type="text/javascript"></script>

		</head>

		<body>
                     
                          <xsl:for-each select="/keywords/word">
                           <b><xsl:value-of select="/keywords/word"/></b><br/>
                           <button onclick="$('.answer').toggle()">Toggle Definintions</button><br/>
                           <span class="answer" style="display: none;"><xsl:value-of select="/keywords/word/@definition"/></span><br/>
                            <br/>
                          </xsl:for-each>
		</body>
	</html>
</xsl:template>

</xsl:stylesheet>