import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
