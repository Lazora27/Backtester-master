import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BollingerPercentB': 1.0
        })
    )
