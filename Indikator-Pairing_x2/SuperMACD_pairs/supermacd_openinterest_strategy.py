import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und OpenInterest
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'OpenInterest': 1.0
        })
    )
