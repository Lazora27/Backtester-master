import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'BuyingPressure': 1.0
        })
    )
