import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AdaptiveATR': 1.0
        })
    )
