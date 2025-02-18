import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'GannSquareReversal': 1.0
        })
    )
