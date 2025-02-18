import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'BalanceMomentum': 1.0
        })
    )
