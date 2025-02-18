import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
