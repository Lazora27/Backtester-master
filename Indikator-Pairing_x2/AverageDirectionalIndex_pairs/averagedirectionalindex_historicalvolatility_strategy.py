import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
