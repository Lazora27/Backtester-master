import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'PriceSquawk': 1.0
        })
    )
