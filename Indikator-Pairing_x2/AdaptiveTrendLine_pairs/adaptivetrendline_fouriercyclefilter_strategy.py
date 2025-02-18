import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
