import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
