import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BollingerPercentB': 1.0
        })
    )
