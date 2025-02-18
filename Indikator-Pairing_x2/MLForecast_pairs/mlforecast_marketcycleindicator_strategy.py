import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
