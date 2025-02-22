from model_mapping import MODEL_NAME_MAPPING
import subprocess


def main():
    for model_family in MODEL_NAME_MAPPING:
        run_command_no_xla = (
            f"python run_benchmark.py --model_family {model_family} --log_wandb"
        )
        run_command_xla = (
            f"python run_benchmark.py --model_family {model_family} --xla --log_wandb"
        )
        for command in [run_command_no_xla, run_command_xla]:
            _ = subprocess.run(command.split())


if __name__ == "__main__":
    main()
