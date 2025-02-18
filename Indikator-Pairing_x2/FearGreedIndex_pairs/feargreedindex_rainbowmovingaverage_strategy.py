import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
