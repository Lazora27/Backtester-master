import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
