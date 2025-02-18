import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
