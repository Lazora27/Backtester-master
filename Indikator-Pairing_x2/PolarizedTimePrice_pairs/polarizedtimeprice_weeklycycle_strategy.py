import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'WeeklyCycle': 1.0
        })
    )
