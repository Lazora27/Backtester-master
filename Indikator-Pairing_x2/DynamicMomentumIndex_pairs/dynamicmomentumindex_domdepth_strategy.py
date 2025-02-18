import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und DOMDepth
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'DOMDepth': 1.0
        })
    )
