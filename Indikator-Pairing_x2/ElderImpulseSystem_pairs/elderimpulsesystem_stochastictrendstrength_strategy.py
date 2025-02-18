import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
