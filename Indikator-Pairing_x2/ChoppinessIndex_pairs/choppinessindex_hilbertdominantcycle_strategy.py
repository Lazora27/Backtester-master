import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
