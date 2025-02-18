import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BalanceMomentum': 1.0
        })
    )
