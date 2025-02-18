import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
