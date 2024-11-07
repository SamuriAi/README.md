# Inference code generated from the JSON schema spec in @huggingface/tasks.
#
# See:
#   - script: https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/scripts/inference-codegen.ts
#   - specs:  https://github.com/huggingface/huggingface.js/tree/main/packages/tasks/src/tasks.
from dataclasses import dataclass
from typing import Any, Dict, Literal, Optional

from .base import BaseInferenceType


SummarizationTruncationStrategy = Literal["do_not_truncate", "longest_first", "only_first", "only_second"]


@dataclass
class SummarizationParameters(BaseInferenceType):
    """Additional inference parameters.
    Additional inference parameters for summarization.
    """

    clean_up_tokenization_spaces: Optional[bool] = None
    """Whether to clean up the potential extra spaces in the text output."""
    generate_parameters: Optional[Dict[str, Any]] = None
    """Additional parametrization of the text generation algorithm."""
    truncation: Optional["SummarizationTruncationStrategy"] = None
    """The truncation strategy to use."""


@dataclass
class SummarizationInput(BaseInferenceType):
    """Inputs for Summarization inference"""

    inputs: str
    """The input text to summarize."""
    parameters: Optional[SummarizationParameters] = None
    """Additional inference parameters."""


@dataclass
class SummarizationOutput(BaseInferenceType):
    """Outputs of inference for the Summarization task"""

    summary_text: str
    """The summarized text."""