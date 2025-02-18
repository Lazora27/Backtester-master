import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'EaseOfMovement': 1.0
        })
    )
