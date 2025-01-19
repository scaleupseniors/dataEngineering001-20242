ENVIRONMENT ?= dev 
PROJECT_ID ?= bridges-vibrations-$(ENVIRONMENT)
REGION ?= us-central1

CODE_BUCKET_NAME ?= sif-med-lakehouse-apps-data-$(ENVIRONMENT)
RAW_BUCKET_NAME ?= sif-med-lakehouse-raw-data-$(ENVIRONMENT)
TRUSTED_BUCKET_NAME ?= sif-med-lakehouse-trusted-data-$(ENVIRONMENT)
BUCKETS ?= $(CODE_BUCKET_NAME) $(RAW_BUCKET_NAME) $(TRUSTED_BUCKET_NAME)

DATAPROC_TEMPLATE ?= dp_lakehouse_workflow
DATAPROC_TEMPLATE_NAME ?= $(DATAPROC_TEMPLATE)_$(ENVIRONMENT)
DATAPROC_INSTANTIATE_TEMPLATE_URL ?= https://dataproc.googleapis.com/v1/projects/$(PROJECT_ID)/regions/us-central1/workflowTemplates/$(DATAPROC_TEMPLATE_NAME):instantiate?alt=json

### Cloud Scheduler config vars
CLOUD_SCHEDULER_JOB_NAME ?= cs-abast-carga-datex-scheduler-$(ENVIRONMENT)
CLOUD_SCHEDULER_JOB_SCHEDULE ?= "0 6 * * *" #6 am every day
CLOUD_SCHEDULER_JOB_RETRY_ATTEMPTS ?= 3
CLOUD_SCHEDULER_JOB_RETRY_ATTEMPT_DEADLINE ?= "30m"
CLOUD_SCHEDULER_JOB_MAX_BACKOFF ?= "1d"
CLOUD_SCHEDULER_JOB_MIN_BACKOFF ?= "1h"
CLOUD_SCHEDULER_JOB_MAX_RETRY_DURATION ?= "3h"
CLOUD_SCHEDULER_JOB_MAX_DOUBLINGS ?= "5"
CLOUD_SCHEDULER_SERVICE_ACCOUNT ?= "sa-$(ENVIRONMENT)-scheduler-orchestration@bridges-vibrations-$(ENVIRONMENT).iam.gserviceaccount.com"
CLOUD_SCHEDULER_SERVICE_ACCOUNT_NAME ?= "sa-$(ENVIRONMENT)-scheduler-orchestration"
CLOUD_SCHEDULER_CUSTOM_ROLE_ID ?= scheduler_orchestration_custom_role
CLOUD_SCHEDULER_CUSTOM_ROLE_NAME ?= "Scheduler Orchestration Custom Role"

### BigQuery config vars
BIGQUERY_DATASET ?= trusted_mobile_app_external_tables
BIGQUERY_TABLE_NAME ?= MobileApp


all: setup_dependencies setup_dataproc setup_cloud_scheduler setup_big_query

### Step 1
setup_dependencies: create_buckets build_code

create_buckets:
	@$(foreach BUCKET,$(BUCKETS),\
	gsutil mb -l $(REGION) gs://$(BUCKET);\
	echo "\e[32mCreated $(BUCKET) bucket\e[0m";\
	)

build_code:
	@echo ""
	@mkdir ../dist
	@cp ../src/main.py ../dist
	@cp ../src/conf/config.yml ../dist
	@cp -r ../src/shared ../dist && cd ../dist && zip -r shared.zip . && rm -rf shared
	@pip install -r ../requirements.txt -t ../dist/libs && cd ../dist/libs && zip -r -D ../libs.zip .
	@cd ../dist && rm -rf libs
	@gsutil -m cp -r ../dist gs://$(CODE_BUCKET_NAME)/$(DATAPROC_TEMPLATE)_code/
	@echo "\e[32mCode and dependencies have been packaged successfully\e[0m"

## Step 2
setup_dataproc: enable_dataproc_api create_dataproc_template instantiate_dataproc_template

enable_dataproc_api:
	@gcloud services enable dataproc.googleapis.com

create_dataproc_template:
	@echo "\e[32mImporting Dataproc ${DATAPROC_TEMPLATE_NAME} template\e[0m"
	@gcloud dataproc workflow-templates import $(DATAPROC_TEMPLATE_NAME) \
		--source=./$(DATAPROC_TEMPLATE).yaml \
		--region=$(REGION) \
		--quiet;
	@echo "\e[32mDataproc ${DATAPROC_TEMPLATE_NAME} template imported correctly\e[0m"

instantiate_dataproc_template:
	@gcloud dataproc workflow-templates instantiate $(DATAPROC_TEMPLATE_NAME) \
		--region=$(REGION)

### Step 3
setup_cloud_scheduler: enable_cloud_scheduler create_custom_role_scheduler \
create_scheduler_service_account give_scheduler_iam_role schedule_dataproc_execution

enable_cloud_scheduler:
	@gcloud services enable cloudscheduler.googleapis.com

create_custom_role_scheduler:
	@gcloud iam roles create $(CLOUD_SCHEDULER_CUSTOM_ROLE_ID) \
		--project=$(PROJECT_ID) \
		--title=$(CLOUD_SCHEDULER_CUSTOM_ROLE_NAME) \
		--permissions="iam.serviceAccounts.actAs,dataproc.workflowTemplates.instantiate"

create_scheduler_service_account:
	@gcloud iam service-accounts create $(CLOUD_SCHEDULER_SERVICE_ACCOUNT_NAME) \
		--display-name="$(CLOUD_SCHEDULER_SERVICE_ACCOUNT)"

give_scheduler_iam_role:
	@gcloud projects add-iam-policy-binding $(PROJECT_ID) \
		--member="serviceAccount:$(CLOUD_SCHEDULER_SERVICE_ACCOUNT)" \
		--role="projects/$(PROJECT_ID)/roles/$(CLOUD_SCHEDULER_CUSTOM_ROLE_ID)"

schedule_dataproc_execution:
	@gcloud scheduler jobs create http $(CLOUD_SCHEDULER_JOB_NAME) \
		--location=$(REGION) \
		--schedule=$(CLOUD_SCHEDULER_JOB_SCHEDULE) \
		--uri=$(DATAPROC_INSTANTIATE_TEMPLATE_URL) \
		--max-retry-attempts=$(CLOUD_SCHEDULER_JOB_RETRY_ATTEMPTS) \
		--attempt-deadline=$(CLOUD_SCHEDULER_JOB_RETRY_ATTEMPT_DEADLINE) \
		--max-backoff=$(CLOUD_SCHEDULER_JOB_MAX_BACKOFF) \
		--min-backoff=$(CLOUD_SCHEDULER_JOB_MIN_BACKOFF) \
		--max-retry-duration=$(CLOUD_SCHEDULER_JOB_MAX_RETRY_DURATION) \
		--max-doublings=$(CLOUD_SCHEDULER_JOB_MAX_DOUBLINGS) \
		--time-zone="America/Bogota" \
		--http-method="POST" \
		--headers=User-Agent=Google-Cloud-Scheduler \

### Step 4
setup_big_query: create_bq_dataset create_bq_table

create_bq_dataset:
	@bq mk --dataset \
		--location=$(REGION) \
		--project_id=$(PROJECT_ID) \
		$(BIGQUERY_DATASET)

create_bq_table:
	@bq mk --table \
		--external_table_definition=@PARQUET=gs://$(TRUSTED_BUCKET_NAME)/MOBILE_APP/part*.parquet "$(PROJECT_ID):$(BIGQUERY_DATASET).$(BIGQUERY_TABLE_NAME)"