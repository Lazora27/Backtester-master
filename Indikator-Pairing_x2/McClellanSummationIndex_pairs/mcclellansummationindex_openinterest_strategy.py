import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
