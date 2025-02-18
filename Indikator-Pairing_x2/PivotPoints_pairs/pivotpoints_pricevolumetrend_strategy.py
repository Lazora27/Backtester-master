import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
