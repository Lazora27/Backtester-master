import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
