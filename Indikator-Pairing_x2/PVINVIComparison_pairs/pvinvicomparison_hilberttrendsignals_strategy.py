import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
