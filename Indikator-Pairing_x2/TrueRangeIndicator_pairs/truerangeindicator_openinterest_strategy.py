import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'OpenInterest': 1.0
        })
    )
