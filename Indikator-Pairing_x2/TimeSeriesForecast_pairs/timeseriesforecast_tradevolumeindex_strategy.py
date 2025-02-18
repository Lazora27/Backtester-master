import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
