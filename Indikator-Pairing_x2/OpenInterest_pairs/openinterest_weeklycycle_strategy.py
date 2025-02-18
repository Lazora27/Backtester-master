import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'WeeklyCycle': 1.0
        })
    )
