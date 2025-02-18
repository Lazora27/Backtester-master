import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
