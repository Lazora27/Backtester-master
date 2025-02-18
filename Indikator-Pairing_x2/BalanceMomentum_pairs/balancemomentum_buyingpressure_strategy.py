import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BuyingPressure': 1.0
        })
    )
