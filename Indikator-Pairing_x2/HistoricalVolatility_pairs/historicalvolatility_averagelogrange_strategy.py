import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'AverageLogRange': 1.0
        })
    )
