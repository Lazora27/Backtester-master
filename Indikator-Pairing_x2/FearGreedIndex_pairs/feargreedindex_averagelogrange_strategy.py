import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
