# Initial setup
To help setup a development environment, you can either install the dependencies manually, or execute the Windows PowerShell script init.ps1 which uses [Chocolatey](https://chocolatey.org/docs/getting-started) to help install the necessary dependencies on your Windows machine. This has been tested on a [Windows 10 virtual machine](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/) with a 2 month license, but should work just as well on a local Windows 10 installation.

## Setup via PowerShell script
The following steps should be executed in a PowerShell session run as an Administrator.
 
First, ensure PowerShell has sufficient permissions to run the initialisation script. You can check this by running the following command in PowerShell:
`Get-ExecutionPolicy -List`

If ExecutionPolicy for CurrentUser is **not** Unrestricted, run the following command:
`Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`

You should then be able to run the `init.ps1` script and follow the setup steps in the prompt.