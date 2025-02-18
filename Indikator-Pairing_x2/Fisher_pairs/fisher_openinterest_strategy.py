import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und OpenInterest
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'OpenInterest': 1.0
        })
    )
