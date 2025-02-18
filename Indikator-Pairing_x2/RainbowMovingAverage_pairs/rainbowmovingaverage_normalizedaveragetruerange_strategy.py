import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_NormalizedAverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und NormalizedAverageTrueRange
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'NormalizedAverageTrueRange': 1.0
        })
    )
