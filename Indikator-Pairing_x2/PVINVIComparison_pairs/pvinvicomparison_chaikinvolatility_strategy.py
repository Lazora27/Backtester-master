import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
