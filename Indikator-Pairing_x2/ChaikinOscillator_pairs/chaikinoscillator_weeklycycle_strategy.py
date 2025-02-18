import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
