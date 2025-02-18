import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und BarStrength
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'BarStrength': 1.0
        })
    )
