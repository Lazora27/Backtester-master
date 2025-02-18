import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'WeeklyCycle': 1.0
        })
    )
