import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'IntradayIntensity': 1.0
        })
    )
