import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
