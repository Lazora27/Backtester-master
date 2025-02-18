import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'BalanceMomentum': 1.0
        })
    )
