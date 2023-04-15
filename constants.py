
site_url = "https://directionshealth.sharepoint.com"
# load from config.prod.json / env client id and client secret
KEY_SHAREPOINT_CLIENTID ='OUTPTCOMPOSR_SPCLID'
KEY_SHAREPOINT_SECRET   ='OUTPTCOMPOSR_SPSEC'

root_template_folder = 'template_fragments'
STRFORMAT_OUTFILENAME = "SLK_AssessmentType_ClientType"

MAP_FIELD_TRANSLATIONS = {
    'PartitionKey': 'SLK',
    'Past4WkEngagedInOtheractivitiesVoluntaryWorkDays': 'VoluntaryWorkDays',
    'Past4WkEngagedInOtheractivitiesVoluntaryWorkFrequency': 'VoluntaryWorkFrequency',
    'Past4WkEngagedInOtheractivitiesPaidWorkDays':'PaidWorkDays',
    'Past4WkEngagedInOtheractivitiesPaidWorkFrequency':'PaidWorkFrequency',
    'Past4WkEngagedInOtheractivitiesStudy-college,schoolorvocationaleducationFrequency':'StudyFrequency',
    'Past4WkEngagedInOtheractivitiesStudy-college,schoolorvocationaleducationDays':'StudyDays',
    'Past4WkEngagedInOtheractivitiesLookingafterchildrenFrequency' : 'LookingafterchildrenFrequency',
    'Past4WkEngagedInOtheractivitiesLookingafterchildrenDays':'LookingafterchildrenDays'
    
}

SURVEY_TYPE_MAP = {
            'InitialAssessment': "INAS",
            'ITSPReview': "ITSP",
            'ArcadiaITSPReview': "ITSP",
            'SupplementaryIntakeAssessment': "SITK",
            'PostTreatmentAssessment': "POTA",
            'PsyReview': "ITSP",
            'PsyEnd': "PYND"
          }

BLPRNT_PROGRAM_MAPPING = {  
  'TSS': 'ACTAODCounsellor',
  'ARCA': 'ResiRehab',
  'COCO': 'PrePostRehab',
  # 'ALONGSIDE':
  'PSYACT': 'Psychologist',
  'PSYNSW': 'Psychologist',
  # 'BUTTITOUT'
  'BEGAPATH': 'NSWPathways',
  'EUROPATH': 'NSWPathways',
  'MONPATH': 'NSWPathways',
  'GOLBGNRL': 'NSWPathways',
  'GOLICE': 'NSWPathways',
  'MURMICE': 'NSWPathways',
  'MURMPP': 'NSWPathways',
  'MURMWIO': 'NSWPathways',
  # 'SAPPHIRE': 'SAPPHIRE',

}