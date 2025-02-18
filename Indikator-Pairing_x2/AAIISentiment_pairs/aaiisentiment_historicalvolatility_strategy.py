import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
