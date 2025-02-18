import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und CyberCycle
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'CyberCycle': 1.0
        })
    )
