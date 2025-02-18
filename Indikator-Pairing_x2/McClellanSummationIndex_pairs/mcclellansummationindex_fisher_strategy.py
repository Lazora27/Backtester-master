import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und Fisher
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'Fisher': 1.0
        })
    )
