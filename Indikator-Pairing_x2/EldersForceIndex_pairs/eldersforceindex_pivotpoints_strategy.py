import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
