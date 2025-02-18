import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
