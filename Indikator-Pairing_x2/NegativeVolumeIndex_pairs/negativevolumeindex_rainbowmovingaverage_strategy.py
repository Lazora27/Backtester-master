import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
