import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
