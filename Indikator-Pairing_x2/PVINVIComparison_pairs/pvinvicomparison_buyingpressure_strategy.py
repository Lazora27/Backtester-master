import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BuyingPressure': 1.0
        })
    )
