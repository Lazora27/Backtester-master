import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
