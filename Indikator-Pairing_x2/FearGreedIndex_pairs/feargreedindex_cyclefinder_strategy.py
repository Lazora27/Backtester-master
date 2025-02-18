import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
