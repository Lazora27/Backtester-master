import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und MovingAverage
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'MovingAverage': 1.0
        })
    )
