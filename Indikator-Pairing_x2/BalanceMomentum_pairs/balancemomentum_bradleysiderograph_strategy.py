import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'BradleySiderograph': 1.0
        })
    )
