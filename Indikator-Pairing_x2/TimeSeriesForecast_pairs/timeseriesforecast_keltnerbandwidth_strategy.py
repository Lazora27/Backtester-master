import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
