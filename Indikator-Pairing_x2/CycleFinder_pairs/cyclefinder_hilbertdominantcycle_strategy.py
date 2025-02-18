import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
