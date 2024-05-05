<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:ns1="ns1:test"
                xmlns:ns2="ns2:test">

    <!--    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"-->
    <!--                    xmlns:ns1="ns1:test:xslt_in.xml"-->
    <!--                    xmlns:ns2="ns2:test:xslt_in.xml">-->
    <xsl:output method="xml" indent="yes" omit-xml-declaration="yes"/>

    <xsl:template match="ns1:input">
        <output>
            <xsl:apply-templates/>
        </output>
    </xsl:template>

    <xsl:template match="ns1:element">
        <element>
            <xsl:attribute name="id">
                <xsl:value-of select="@id"/>
            </xsl:attribute>
            <xsl:apply-templates/>
        </element>
    </xsl:template>

    <xsl:template match="ns2:*">
        <xsl:element name="{local-name()}">
            <xsl:attribute name="element_id">
                <xsl:value-of select="../@id"/>
            </xsl:attribute>
            <xsl:value-of select="."/>
        </xsl:element>
    </xsl:template>

</xsl:stylesheet>
