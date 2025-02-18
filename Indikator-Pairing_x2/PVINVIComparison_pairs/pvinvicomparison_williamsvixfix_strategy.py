import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
