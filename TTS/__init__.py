import os

# Backfill isin_mps_friendly for transformers 4.40.0+ compatibility
# (transformers removed this function but older versions of coqui-tts expect it)
try:
    from transformers.pytorch_utils import isin_mps_friendly
except ImportError:
    import torch
    def isin_mps_friendly(elements, test_elements):
        return torch.isin(elements, test_elements)
    import transformers.pytorch_utils
    transformers.pytorch_utils.isin_mps_friendly = isin_mps_friendly

with open(os.path.join(os.path.dirname(__file__), "VERSION"), "r", encoding="utf-8") as f:
    version = f.read().strip()

__version__ = version
