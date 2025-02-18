import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
