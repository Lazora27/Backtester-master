import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ExtensionProjections': 1.0
        })
    )
