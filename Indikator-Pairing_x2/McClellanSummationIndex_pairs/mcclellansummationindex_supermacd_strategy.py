import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
