import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und GannAngles
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'GannAngles': 1.0
        })
    )
