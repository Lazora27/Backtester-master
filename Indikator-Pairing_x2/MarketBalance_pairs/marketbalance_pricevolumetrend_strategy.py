import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
