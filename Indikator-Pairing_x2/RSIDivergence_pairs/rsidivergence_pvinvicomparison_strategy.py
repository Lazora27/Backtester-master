import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PVINVIComparison': 1.0
        })
    )
