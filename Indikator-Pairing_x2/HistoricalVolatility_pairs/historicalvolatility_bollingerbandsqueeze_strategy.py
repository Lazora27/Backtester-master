import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
