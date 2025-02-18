import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'VolatilityIndex': 1.0
        })
    )
