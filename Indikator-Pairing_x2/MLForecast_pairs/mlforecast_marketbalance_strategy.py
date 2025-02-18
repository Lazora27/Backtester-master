import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MarketBalance
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MarketBalance': 1.0
        })
    )
