import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
