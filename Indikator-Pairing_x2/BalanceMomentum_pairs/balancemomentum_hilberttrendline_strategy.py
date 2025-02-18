import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'HilbertTrendline': 1.0
        })
    )
