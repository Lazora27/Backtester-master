import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
