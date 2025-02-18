import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
