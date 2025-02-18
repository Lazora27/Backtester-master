import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
