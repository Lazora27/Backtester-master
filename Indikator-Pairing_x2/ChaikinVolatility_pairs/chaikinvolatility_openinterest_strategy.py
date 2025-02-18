import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'OpenInterest': 1.0
        })
    )
