import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
