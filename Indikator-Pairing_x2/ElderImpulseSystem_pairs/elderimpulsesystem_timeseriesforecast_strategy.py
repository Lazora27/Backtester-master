import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
