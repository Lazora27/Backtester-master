import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PVINVIComparison': 1.0
        })
    )
