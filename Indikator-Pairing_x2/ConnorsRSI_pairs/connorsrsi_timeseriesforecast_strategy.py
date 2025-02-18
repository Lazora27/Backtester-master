import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
