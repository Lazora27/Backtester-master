import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
