import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
