import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
