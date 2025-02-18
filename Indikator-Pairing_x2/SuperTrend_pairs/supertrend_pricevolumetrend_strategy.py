import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
