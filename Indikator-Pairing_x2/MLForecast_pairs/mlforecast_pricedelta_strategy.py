import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PriceDelta
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PriceDelta': 1.0
        })
    )
