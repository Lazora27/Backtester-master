import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und BollingerBands
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'BollingerBands': 1.0
        })
    )
