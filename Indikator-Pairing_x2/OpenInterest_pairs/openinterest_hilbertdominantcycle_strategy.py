import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
