import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und CCITurbo
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'CCITurbo': 1.0
        })
    )
