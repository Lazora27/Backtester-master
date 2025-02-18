import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PriceSquawk': 1.0
        })
    )
