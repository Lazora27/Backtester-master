import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CenterOfGravity': 1.0
        })
    )
