import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'CycleFinder': 1.0
        })
    )
