import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ChandeTrendScore_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ChandeTrendScore
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ChandeTrendScore': 1.0
        })
    )
