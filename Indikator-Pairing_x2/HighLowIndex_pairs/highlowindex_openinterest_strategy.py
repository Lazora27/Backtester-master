import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
