import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'CenterOfGravity': 1.0
        })
    )
