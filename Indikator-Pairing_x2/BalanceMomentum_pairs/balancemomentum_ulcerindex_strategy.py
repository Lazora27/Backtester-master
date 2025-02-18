import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'UlcerIndex': 1.0
        })
    )
