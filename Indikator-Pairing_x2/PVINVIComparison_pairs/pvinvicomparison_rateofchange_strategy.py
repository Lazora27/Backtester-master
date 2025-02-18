import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und RateOfChange
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'RateOfChange': 1.0
        })
    )
