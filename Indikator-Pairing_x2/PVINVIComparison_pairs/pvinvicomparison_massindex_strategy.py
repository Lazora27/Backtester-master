import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MassIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MassIndex': 1.0
        })
    )
