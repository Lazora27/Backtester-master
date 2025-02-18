import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalVolatility_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalVolatility und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HistoricalVolatility': 1.0,
            'IntradayIntensity': 1.0
        })
    )
