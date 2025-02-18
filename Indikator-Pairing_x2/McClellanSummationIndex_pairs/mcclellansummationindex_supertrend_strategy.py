import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und SuperTrend
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'SuperTrend': 1.0
        })
    )
