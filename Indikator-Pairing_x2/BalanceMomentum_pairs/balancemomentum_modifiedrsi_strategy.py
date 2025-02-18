import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ModifiedRSI': 1.0
        })
    )
