import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CycleFinder
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CycleFinder': 1.0
        })
    )
