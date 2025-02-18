import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und OpenInterest
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'OpenInterest': 1.0
        })
    )
