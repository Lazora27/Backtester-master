import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
