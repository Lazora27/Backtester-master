import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'OpenInterest': 1.0
        })
    )
