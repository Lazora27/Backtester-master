import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ArmsIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ArmsIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ArmsIndex': 1.0
        })
    )
