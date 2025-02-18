import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
