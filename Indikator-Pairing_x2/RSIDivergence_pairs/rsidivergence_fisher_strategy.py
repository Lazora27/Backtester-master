import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_Fisher_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und Fisher
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'Fisher': 1.0
        })
    )
