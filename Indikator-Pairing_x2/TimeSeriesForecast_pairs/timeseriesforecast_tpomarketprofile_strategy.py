import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
