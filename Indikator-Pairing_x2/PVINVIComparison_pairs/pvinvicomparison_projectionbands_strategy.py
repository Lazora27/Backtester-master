import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ProjectionBands': 1.0
        })
    )
