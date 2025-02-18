import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
