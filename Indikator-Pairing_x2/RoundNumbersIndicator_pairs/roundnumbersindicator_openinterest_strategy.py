import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
