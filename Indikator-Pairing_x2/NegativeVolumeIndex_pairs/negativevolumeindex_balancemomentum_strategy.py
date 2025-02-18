import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'BalanceMomentum': 1.0
        })
    )
