import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BalanceMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BalanceMomentum
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BalanceMomentum': 1.0
        })
    )
