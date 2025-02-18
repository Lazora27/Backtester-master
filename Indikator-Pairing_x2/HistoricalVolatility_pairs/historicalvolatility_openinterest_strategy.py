import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und OpenInterest
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'OpenInterest': 1.0
        })
    )
