import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
