import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
