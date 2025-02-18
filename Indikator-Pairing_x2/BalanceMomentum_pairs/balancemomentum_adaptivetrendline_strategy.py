import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
