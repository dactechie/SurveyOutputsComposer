# SurveyOutputsComposer

Dynamically compose a summary .docx file using custom document fragments(.docx) and blueprints (.json) configuration.

Uses the JSON output from a SurveyJS submission.

## Left at :

- Created ProgramMapping.json file
- Copied Arcadia ITSP full template into : SurveyOutputsComposer\template_fragments\Programs\ResiRehab

# Change to :

ProgramMapping + SurveyType + ClientType

          export const SURVEY_TYPE_MAP = {
            // Survey title : RowKey code
            InitialAssessment: "INAS",
            ITSPReview: "ITSP",
            ArcadiaITSPReview: "ITSP",            -> Role: ResiRehab
            SupplementaryIntakeAssessment: "SITK",  --> Role ? PrePostRehab
            PostTreatmentAssessment: "POTA",       --> Role ? PrePostRehab
            PsyReview: "ITSP",            -> Role: Psychologist
            PsyEnd: "PYND"
          };

## Folder for each combo with Word templates withn and one BluePrint template for each

/ Example: blueprint / TSS_INAS_Ownuse.json

/Blueprints:

- TSS_INAS_OwnUse.json # dictates order and whether to show sections or NOT , if they are empty.

- NSWPathways_INAS_ownuse.json
  for all NSW pathways Programs
- SAPPHIRE_ITSP_othersuse.json

* base/common fragments: Intro, FinalChecklist
* fragments specific to sapphire : 'SAPPHIRE/INAS/OthersUse/'
* get_role_based_sections-> Roles/NSWCounsellor

- COCO_SITK_ownuse.json
- COCO_POTA_ownuse.json
- ARCA_ITSP_ownuse.json

/fragments
/Common
Intro.docx
FinalChecklist.docx

               /TSS_INAS_OwnUse

/TSS
/INAS
/OwnUse
/ITSP

Question : Should I organise Fragment in subfoders /INAS /ITSP
30% common questions

    based on Directions Health Intranet - ICT\ANSA\Documentation\BreakdownOfFieldsBySurveyTemplateType.pptx

## Next:

### Maintainence:

Do logging , esp with network calls.

## TODO :

    Translate Dropdown values: C:\Users\aftab.jalal\dev\SurveyOutputsComposer\main_use_surveyjs_qjson.py
