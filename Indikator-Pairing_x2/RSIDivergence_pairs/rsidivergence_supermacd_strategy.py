import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und SuperMACD
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'SuperMACD': 1.0
        })
    )
