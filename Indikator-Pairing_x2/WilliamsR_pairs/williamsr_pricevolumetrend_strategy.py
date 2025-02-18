import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
