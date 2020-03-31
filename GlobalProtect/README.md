Forescout eyeExtend Connect GlobalProtect App README.md
 

## Legal Notice
© 2020 Forescout Technologies, Inc. All rights reserved. Forescout Technologies, Inc. is a Delaware corporation.
A list of our trademarks and patents can be found at https://www.Forescout.com/company/legal/intellectual-property-patents-trademarks.
Other brands, products, or service names may be trademarks or service marks of their respective owners.

## About the eyeExtend Connect GlobalProtect App
The App gather users and endpoints information that connected to GlobalProtect servers. User can also use policies or
actions to disconnect user from the GlobalProtect Server. The App uses admin management interface to access the
GlobalProtect server.

## Requirements
The App supports:
- PANOS 8.1
- Forescout CounterACT 8.2
- Forescout eyeExtend Connect 1.1
- See license.txt file for license information

## User Interface
You can refer to the Forescout eyeExtend Connect Module: Connect Application Building Guide, in particular the
sections on ”Define system.conf File” and “User Interface Details”.
### Panels
#### Device
User can add GlobalProtect server to the App.
- Server name shall be the GlobalProtect server in "https://<GlobalProtectServerNameOrIP>" format
- User shall be admin that can access GlobalProtect web APIs via management interface
- Password shall be the admin password that can be used to accrue token for the web API call to GlobalProtect server
- User can test the device by clicking TEST button after applying changes.
- User can add multiple devices, they need to be unique and has a dedicated focal appliance.

#### Focal appliance
Each device shall run on one dedicated focal appliance.

#### Rate-limited API Count
- User can set rate-limiter for the API allowed to the GlobalProtect per unit time.
- Default in the App is allowing up to 100 API calls per second.
- Range is 1 to 1000 APIs.

#### Predefined fields used panels
- Certification validation
- Authorization
- Rate limiter

### Test button
- Test is enabled by default.
- Device info need to be saved (applied) before test can be successfully run.

## Manage the App
### Import
- User can import the GlobalProtect Connect App via eyeExtend Connect module
- App file shall look like GlobalProtectApp.ECP which is signed

## Start and Stop App
- User can start and stop the GlobalProtect App
- When the App is stopped, all properties resolve, actions and policy are suspended.

### Remove App
- User can remove the App if no longer needed
- User need to delete the GlobalProtect policy first to remove the App.

## Policy Templates
- There is a default GlobalProtect Template
- After importing the App. the policy can be find under Policy > Add > GlobalProtect > GlobalProtect Policy
- User can use the default policy to resolve properties from endpoint on a schedule.
- User need to define rules to disconnect a user from GlobalProtect server.

## Properties
There are a few properties gathered from the GlobalProtect server for the endpoint.
- GlobalProtect User's Domain 
- GlobalProtect Computer Name
- GlobalProtect IP Type
- GlobalProtect User
- GlobalProtect Gateway
- GlobalProtect Client Type, such as: Microsoft Windows 7 Ultimate Edition Service Pack 1, 64-bit 

## Actions
User can disconnect a connected GlobalProtect from the endpoint. If the user is disconnected from GlobalProtect,
some endpoint properties can't be resolved. Error would indicate that user is disconnected.

Disconnect user action is a one-time actions. User needs to be reconnect to the GlobalProtect server for resolve and
disconnect actions to work properly again.

## Scripts
There are three scripts and a library file.
- globalprotect_disconnect_user.py
User can disconnect a connected user from GlobalProtect.
- globalprotect_resolve.py
User can get the GlobalProtect properties of the an endpoint.
- globalprotect_test.py
User can test the connection to GlobalProtect server with defined device.
- globalprotect_library.py
Library files scripts use.

## Notes
- When user in an endpoint is disconnected to GlobalProtect, there is an error indicating that user might be disconnected
during resolve. And the disconnected user shall fail on a disconnected endpoint action.
- User on the endpoint needs to reconnect to GlobalProtect to resolve properties or take actions correctly again.
- The Disconnect User will only work if the GlobalProtect(VPN) is disabled from trying to establish a connection again.
The GlobalProtect admin should not setup the configuration for "user-logon (Always-on)" as the connect method.

## Licenses
This App bundles with a license.txt file. Please review the license.txt file.