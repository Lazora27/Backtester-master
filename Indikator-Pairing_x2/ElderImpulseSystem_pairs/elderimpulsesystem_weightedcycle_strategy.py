import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WeightedCycle': 1.0
        })
    )
