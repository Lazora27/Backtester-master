import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
