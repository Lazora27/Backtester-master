import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
