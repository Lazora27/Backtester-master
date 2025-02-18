import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
