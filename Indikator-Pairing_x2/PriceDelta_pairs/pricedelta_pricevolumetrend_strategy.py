import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
