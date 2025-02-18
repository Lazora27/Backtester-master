import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'HistoricalATR': 1.0
        })
    )
