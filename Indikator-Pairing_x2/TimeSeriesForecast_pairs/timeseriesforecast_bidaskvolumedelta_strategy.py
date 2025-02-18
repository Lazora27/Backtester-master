import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
