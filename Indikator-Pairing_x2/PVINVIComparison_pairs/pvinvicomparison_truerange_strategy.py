import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TrueRange
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TrueRange': 1.0
        })
    )
