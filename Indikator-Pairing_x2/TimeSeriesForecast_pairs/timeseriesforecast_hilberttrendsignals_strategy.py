import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
