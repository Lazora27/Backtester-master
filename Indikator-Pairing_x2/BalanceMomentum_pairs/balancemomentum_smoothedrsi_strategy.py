import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'SmoothedRSI': 1.0
        })
    )
