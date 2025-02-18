import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
