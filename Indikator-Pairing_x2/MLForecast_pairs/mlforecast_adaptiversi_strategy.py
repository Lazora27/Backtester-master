import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
