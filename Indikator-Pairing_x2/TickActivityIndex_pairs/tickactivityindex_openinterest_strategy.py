import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
