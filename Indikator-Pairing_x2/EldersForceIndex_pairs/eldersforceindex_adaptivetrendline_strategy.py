import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
