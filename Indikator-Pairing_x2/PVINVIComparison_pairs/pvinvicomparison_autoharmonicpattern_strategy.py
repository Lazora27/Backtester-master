import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
