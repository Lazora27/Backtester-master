import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
