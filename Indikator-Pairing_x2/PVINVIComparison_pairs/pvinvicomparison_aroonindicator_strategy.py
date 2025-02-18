import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AroonIndicator': 1.0
        })
    )
