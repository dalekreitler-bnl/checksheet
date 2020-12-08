# checksheet

MX Beamline staff must load sample spreadsheets during beamline alignment/setup which can consume time if the spreadsheet contains errors. It would be useful to run these checks before hand so that staff can focus on beamline setup rather than exception wrangling, hence checksheet.

checksheet is a bash shell script that uses ssh to execute a python script on the compute node r21-001 (nsls2 controls network) in a conda environment that mimics the environment required by LSDC to run the validation check that occurs upon importing a spreadsheet. Checksheet includes code written by John Skinner and Jun Aishima. Checksheet's main functions are:

1) run the validation check that LSDC performs upon importing a spreadsheet
2) read the monogo database on xf17id1-ca1, to check for previously loaded containers
3) print what would have been loaded by LSDC to console


Usage:

checksheet spreadsheet_to_check.xlsx


# Setup

The only setup required is that checksheet must be in the user PATH, so the following path can be added to ~/.bashrc

export PATH=$PATH:/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/bin

**Passwordless usage**
If you want to avoid typing your password over and over for each check then load your public rsa keys from the workstation you are running checksheet on to your r21-001 profile with the following command

cat ~/.ssh/id_rsa.pub | ssh <user>@r21-001 'umask 0077; mkdir -p .ssh; cat >> .ssh/authorized_keys && echo "Key copied"'

**If this fails because you don't have an .ssh profile on the current workstation then run:

ssh-keygen

# Example with proper spreadsheet

checksheet is designed to be executed on one of the beamline workstations, but really can be executed from any node with GPFS access

* Go to GPFS directory that contains spreadsheet that needs to be checked:

cd /GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/test_sheets

* then execute checksheet, works with .xls or .xlsx

checksheet test.xls

Output (the hostkey error is unrelated to checksheet):

dkreitler@xf17id2-ws3:/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/test_sheets$ checksheet test.xls</br>
no matching hostkey found for key ED25519 14:6f:40:26:2a:67:e2:fe:f7:4b:f7:ed:fa:fe:9c:c2</br>
['/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/parseSheet.py', '/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/test_sheets/test.xls']</br>
Executing dry run for importSpreadsheet</br>
Spreadsheet starting with puck NSLS2_4 being created...</br>
NSLS2_4_01 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_02 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_03 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_04 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_05 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_06 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_07 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_08 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_09 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_10 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_11 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_12 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_13 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_14 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_15 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_4_16 would have gone in container NSLS2_4, previously loaded by jjakoncic</br>
NSLS2_24_01 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_02 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_03 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_04 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_05 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_06 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_07 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_08 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_09 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_10 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_11 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_12 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_13 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_14 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_15 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
NSLS2_24_16 would have gone in container NSLS2_24, previously loaded by jjakoncic</br>
ILL_6_01 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_02 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_03 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_04 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_05 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_06 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_07 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_08 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_09 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_10 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_11 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_12 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_13 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_14 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_15 would have gone in container ILL_6, previously loaded by jjakoncic</br>
ILL_6_16 would have gone in container ILL_6, previously loaded by jjakoncic</br>
Spreadsheet would start with NSLS2_4 created with 48 samples</br>

# Example with duplicate error

dkreitler@xf17id2-ws3:/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/test_sheets$ checksheet duplicate_test.xls</br>
no matching hostkey found for key ED25519 14:6f:40:26:2a:67:e2:fe:f7:4b:f7:ed:fa:fe:9c:c2</br>
['/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/parseSheet.py', '/GPFS/CENTRAL/xf17id2/dkreitler/projects/checksheet/test_sheets/duplicate_test.xls']</br>
Executing dry run for importSpreadsheet</br>
Insert spreadsheet aborting due to Exception('duplicate sampleName: sampleName: NSLS2_4_10')
