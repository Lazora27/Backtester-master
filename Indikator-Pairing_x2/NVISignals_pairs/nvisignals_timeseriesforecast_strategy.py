import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
