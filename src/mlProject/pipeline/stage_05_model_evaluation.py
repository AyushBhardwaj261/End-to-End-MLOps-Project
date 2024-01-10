from mlProject import logger
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.config.configuration import ConfigurationManager

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval_config = ModelEvaluation(config=model_eval_config)
        model_eval_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_eval = ModelEvaluationTrainingPipeline()
        model_eval.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e