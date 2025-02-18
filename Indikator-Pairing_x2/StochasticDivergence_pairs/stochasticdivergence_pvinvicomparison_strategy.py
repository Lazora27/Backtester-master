import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PVINVIComparison': 1.0
        })
    )
