import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
