import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SmoothedRSI': 1.0
        })
    )
