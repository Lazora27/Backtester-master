import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BalanceMomentum': 1.0
        })
    )
