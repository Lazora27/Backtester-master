import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DOMDepth
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DOMDepth': 1.0
        })
    )
