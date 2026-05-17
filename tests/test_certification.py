
from dev_utils.certification.telemetry_integrity import verify_batch_normalization

def test_verify_batch_normalization():
    assert verify_batch_normalization([1.0, 2.5, 3.1]) == True
    assert verify_batch_normalization([]) == False
