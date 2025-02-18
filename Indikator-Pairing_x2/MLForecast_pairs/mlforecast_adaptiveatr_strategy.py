import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AdaptiveATR': 1.0
        })
    )
