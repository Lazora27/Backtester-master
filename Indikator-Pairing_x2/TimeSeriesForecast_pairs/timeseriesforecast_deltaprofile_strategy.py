import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'DeltaProfile': 1.0
        })
    )
