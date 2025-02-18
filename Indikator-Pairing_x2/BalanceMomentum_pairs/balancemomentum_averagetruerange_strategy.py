import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AverageTrueRange': 1.0
        })
    )
