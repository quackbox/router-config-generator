from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import SelectField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, IPAddress

class configForm(FlaskForm):
    rtrHostname = StringField(
        'Router Hostname',
        [DataRequired()]
    )
    dnsSuffix = StringField(
        'DNS Suffix',
        [DataRequired()]
    )
    tzName = SelectField(
        'Timezone Name', choices=[('ACST'), ('AEST'), ('AWST')]
    )
    tzOffset = StringField(
        'Timezone offset from UTC',
        [DataRequired()]
    )
    dnsResolverPrimary = StringField(
        'Primary DNS Server',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    dnsResolverSecondary = StringField(
        'Secondary DNS Server',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    rtrAdminUsername = StringField(
        'Router Root Username',
        [DataRequired()]
    )
    rtrAdminPassword = PasswordField(
        'Router Root Password',
        [DataRequired()]
    )
    lanIPAddress = StringField(
        'LAN IP address',
        [IPAddress(ipv4=True, ipv6=True, message='Please enter a valid IPv4 or IPv6 address')]
    )
    lanCidrPrefixSize = SelectField(
        'LAN Prefix Size (CIDR)', choices=[('/31'), ('/30'), ('/29'), ('/28'), ('/27'), ('/26'), ('/25'), ('/24'), ('/23'), ('/22'), ('/21'), ('/20'), ('/19'), ('/18'), ('/17'), ('/16')]
    )
    wanTechnologyType = SelectField(
        'Service Technology Type', choices=[('FTTP'), ('FTTC'), ('HFC'), ('FTTN')]
    )
    wanAuthType = SelectField(
        'Service Authentication Type', choices=[('IPoE (DHCP)'), ('PPPoE (Username/Password)')]
    )
    rtrVendor = SelectField(
        'Router Vendor', choices=[('Cisco')]
    )
    rtrSeries = SelectField(
        'Router Series', choices=[('880'), ('890'), ('1100'), ('1900'), ('2900'), ('4000')]
    )
    generate = SubmitField('Generate Config')
