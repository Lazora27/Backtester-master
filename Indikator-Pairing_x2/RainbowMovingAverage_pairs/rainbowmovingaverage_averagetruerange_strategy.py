import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'AverageTrueRange': 1.0
        })
    )
