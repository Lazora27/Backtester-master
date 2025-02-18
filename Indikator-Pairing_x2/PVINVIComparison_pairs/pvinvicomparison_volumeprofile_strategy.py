import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'VolumeProfile': 1.0
        })
    )
