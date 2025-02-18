import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
