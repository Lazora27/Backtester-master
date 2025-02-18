import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und OpenInterest
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'OpenInterest': 1.0
        })
    )
