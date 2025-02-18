import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DonchianVolatility': 1.0
        })
    )
