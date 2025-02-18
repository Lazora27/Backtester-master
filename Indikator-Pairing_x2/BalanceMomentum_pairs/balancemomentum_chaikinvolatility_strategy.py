import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
