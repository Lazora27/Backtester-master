import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
