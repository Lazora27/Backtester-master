import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
