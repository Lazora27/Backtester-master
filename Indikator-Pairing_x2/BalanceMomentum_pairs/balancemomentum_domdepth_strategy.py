import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und DOMDepth
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'DOMDepth': 1.0
        })
    )
