import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
