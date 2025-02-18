import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MACDHistogram': 1.0
        })
    )
