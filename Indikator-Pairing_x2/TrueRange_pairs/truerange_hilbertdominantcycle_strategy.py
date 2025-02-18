import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
