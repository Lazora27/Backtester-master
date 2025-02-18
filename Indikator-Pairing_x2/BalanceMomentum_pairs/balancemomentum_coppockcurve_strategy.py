import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CoppockCurve': 1.0
        })
    )
