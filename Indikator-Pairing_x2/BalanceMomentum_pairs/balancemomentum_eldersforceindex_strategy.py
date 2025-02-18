import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'EldersForceIndex': 1.0
        })
    )
