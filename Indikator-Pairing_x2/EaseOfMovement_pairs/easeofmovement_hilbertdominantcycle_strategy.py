import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
