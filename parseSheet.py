import sys
import pandas
import db_lib
import sanitize_sheet
import logging
#logger = logging.getLogger(__name__)
staffList = ["jjakoncic","soares","stojanof","dkreitler","elazo","mfuchs"]

def dryrun(func):
    dryrun = True
    def wrapper(*args,**kwargs):
        print(f"Executing dry run for {func.__name__}")
        func(*args,**kwargs)
    return wrapper

def parseSpreadsheet(infilename):
  DataFrame = pandas.read_excel(infilename)
  d = DataFrame.to_dict()
  #logger.info(d)
  return d

def insertSpreadsheetDict(d):
  currentPucks = []
  first_container_name = str(d["puckName"][0]).replace(" ","")
  try:
    sanitize_sheet.check_sampleNames(d["sampleName"].values())
    sanitize_sheet.check_for_duplicate_samples(d["sampleName"].values())
    #sanitize_sheet.check_for_sequence(d["sequence"].values()) #remove for now
    sanitize_sheet.check_proposalNum(d["proposalNum"].values())
  except Exception as e:
    message = f"Insert spreadsheet aborting due to {repr(e)}"
    #logger.error(message)
    print(message)
    return
  print("Spreadsheet starting with puck %s being created..." % first_container_name)
  for i in range (0,len(d["puckName"])): #number of rows in sheet
    container_name = str(d["puckName"][i]).replace(" ","")
    position_s = str(d["position"][i]).replace(" ","")
    position = int(position_s)
    propNum = None
    try:
      propNum_s = str(d["proposalNum"][i]).replace(" ","")
      propNum = int(propNum_s)
    except KeyError:
      pass
    except ValueError:
      propNum = None      
    if (propNum == ''):
      propNum = None
    #logger.warning(propNum)
    item_name1 = str(d["sampleName"][i]).replace(".","_")
    item_name = item_name1.replace(" ","_")    
    modelFilename = str(d["model"][i]).replace(" ","")
    sequenceFilename = str(d["sequence"][i]).replace(" ","")
    for staff in staffList:
        containerUID = db_lib.getContainerIDbyName(container_name,staff)
        staffLoaded = staff
        if containerUID != '':
            break
    #containerUID = db_lib.getContainerIDbyName(container_name)
    if containerUID != '':
   #   logger.info("create container " + str(container_name))
      print(f"{item_name} would have gone in container {container_name}, previously loaded by {staffLoaded}")
    else:
      print(f"{item_name} would have gone in container {container_name}")

   #   containerUID = db_lib.createContainer(container_name,16,owner,"16_pin_puck")
   # sampleUID = db_lib.getSampleIDbyName(item_name,owner) #this line looks like not needed anymore
   #   logger.info("create sample " + str(item_name))
   # sampleUID = db_lib.createSample(item_name,owner,"pin",model=modelFilename,sequence=sequenceFilename,proposalID=propNum)
    if (containerUID not in currentPucks):
   #   db_lib.emptyContainer(containerUID)
      currentPucks.append(containerUID)
   #   logger.info(''.join(["insertIntoContainer ",str(container_name),",","test",",",str(position),",","testID"]))
   # db_lib.insertIntoContainer(container_name, owner, position, sampleUID)
  print(f"Spreadsheet would start with {first_container_name} created with {len(d['puckName'])} samples")
  
@dryrun
def importSpreadsheet(infilename):
  d = parseSpreadsheet(infilename)
  insertSpreadsheetDict(d)

if __name__ == "__main__":

  filename = sys.argv[1]
  print(sys.argv)
  importSpreadsheet(filename)
  

    
