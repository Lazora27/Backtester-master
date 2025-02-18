import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
