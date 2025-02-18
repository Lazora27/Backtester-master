import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
