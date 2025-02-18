import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ParabolicSAR': 1.0
        })
    )
