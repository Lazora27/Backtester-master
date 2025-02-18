import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersCenterOfGravityOscillator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersCenterOfGravityOscillator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'EhlersCenterOfGravityOscillator': {
                'class': EhlersCenterOfGravityOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersCenterOfGravityOscillator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'EhlersCenterOfGravityOscillator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
