import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und MassIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'MassIndex': 1.0
        })
    )
