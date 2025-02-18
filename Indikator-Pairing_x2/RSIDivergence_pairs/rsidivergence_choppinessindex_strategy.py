import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
