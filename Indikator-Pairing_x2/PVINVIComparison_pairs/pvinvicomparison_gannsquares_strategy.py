import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und GannSquares
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'GannSquares': 1.0
        })
    )
