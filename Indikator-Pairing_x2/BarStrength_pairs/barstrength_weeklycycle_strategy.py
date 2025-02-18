import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'WeeklyCycle': 1.0
        })
    )
