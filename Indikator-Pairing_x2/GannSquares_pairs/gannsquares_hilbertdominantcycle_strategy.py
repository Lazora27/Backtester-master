import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
