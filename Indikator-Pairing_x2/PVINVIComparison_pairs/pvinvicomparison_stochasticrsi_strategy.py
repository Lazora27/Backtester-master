import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'StochasticRSI': 1.0
        })
    )
