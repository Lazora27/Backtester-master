import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
