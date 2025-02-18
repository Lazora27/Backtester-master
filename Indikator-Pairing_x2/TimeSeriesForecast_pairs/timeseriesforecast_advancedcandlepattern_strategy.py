import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
