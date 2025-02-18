import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'AccelerationBands': 1.0
        })
    )
