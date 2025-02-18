import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
