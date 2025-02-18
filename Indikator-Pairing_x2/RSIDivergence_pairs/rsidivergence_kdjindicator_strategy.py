import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'KDJIndicator': 1.0
        })
    )
