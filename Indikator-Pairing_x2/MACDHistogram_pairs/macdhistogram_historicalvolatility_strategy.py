import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
