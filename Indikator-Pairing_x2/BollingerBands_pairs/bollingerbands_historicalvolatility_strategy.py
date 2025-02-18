import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
