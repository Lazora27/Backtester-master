import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
