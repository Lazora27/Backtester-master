import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
