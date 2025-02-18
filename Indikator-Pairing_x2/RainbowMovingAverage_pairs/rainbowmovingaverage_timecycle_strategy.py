import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und TimeCycle
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'TimeCycle': 1.0
        })
    )
