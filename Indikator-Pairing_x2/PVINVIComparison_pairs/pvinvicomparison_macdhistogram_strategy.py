import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MACDHistogram': 1.0
        })
    )
