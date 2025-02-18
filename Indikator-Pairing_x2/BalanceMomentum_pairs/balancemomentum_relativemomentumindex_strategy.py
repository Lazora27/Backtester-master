import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
