# Import the Active Directory module
Import-Module ActiveDirectory

# Set the parameters for the new user
$FirstName = "Franz"
$LastName = "Ferdinand"
$DisplayName = "$FirstName $LastName"
$SamAccountName = "ferdinandf"
$UserPrincipalName = "ferdi@GlobeXpower.com"
$Title = "TPS Reporting Lead"
$Department = "TPS"
$Office = "Springfield"
$State = "OR"

# Set the parameters for the new group
$GroupName = "TPSGroup"

# Set the parameters for the new organizational unit (OU)
$OUName = "TPS_OU"

# Create new user
New-ADUser -SamAccountName $SamAccountName -UserPrincipalName $UserPrincipalName -GivenName $FirstName -Surname $LastName -DisplayName $DisplayName -Title $Title -Department $Department -Office $Office -State $State -EmailAddress $UserPrincipalName -Enabled $true -Path "OU=$OUName,DC=yourdomain,DC=com" -AccountPassword (ConvertTo-SecureString -AsPlainText "Password123" -Force) -ChangePasswordAtLogon $true

# Create new group
New-ADGroup -Name $GroupName -GroupCategory Security -GroupScope Global -Path "OU=$OUName,DC=yourdomain,DC=com"

# Create new organizational unit
New-ADOrganizationalUnit -Name $OUName -Path "DC=yourdomain,DC=com"

Write-Host "User, group, and OU created successfully."
