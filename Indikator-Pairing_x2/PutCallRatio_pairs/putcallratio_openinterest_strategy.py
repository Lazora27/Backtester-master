import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'OpenInterest': 1.0
        })
    )
