import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
