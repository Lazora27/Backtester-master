import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
