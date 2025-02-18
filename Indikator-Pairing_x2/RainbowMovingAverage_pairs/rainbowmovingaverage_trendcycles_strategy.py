import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'TrendCycles': 1.0
        })
    )
