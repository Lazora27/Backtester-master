import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
