import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und FisherTransform
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'FisherTransform': 1.0
        })
    )
