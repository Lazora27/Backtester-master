import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
