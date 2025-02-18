import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BalanceMomentum': 1.0
        })
    )
