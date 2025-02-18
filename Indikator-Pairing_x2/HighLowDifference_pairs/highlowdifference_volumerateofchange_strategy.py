import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
