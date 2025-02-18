import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
