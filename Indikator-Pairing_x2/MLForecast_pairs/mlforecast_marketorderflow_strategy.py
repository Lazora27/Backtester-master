import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
