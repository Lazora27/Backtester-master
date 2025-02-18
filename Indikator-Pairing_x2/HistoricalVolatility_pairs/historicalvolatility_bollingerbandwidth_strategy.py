import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
