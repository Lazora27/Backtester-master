import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'EhlersDecycler': 1.0
        })
    )
