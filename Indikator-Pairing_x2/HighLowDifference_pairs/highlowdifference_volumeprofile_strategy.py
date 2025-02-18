import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VolumeProfile': 1.0
        })
    )
