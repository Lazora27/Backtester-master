import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
