import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PVINVIComparison': 1.0
        })
    )
