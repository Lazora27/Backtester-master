import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
