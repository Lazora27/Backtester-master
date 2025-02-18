import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
