import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und TrueRange
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'TrueRange': 1.0
        })
    )
