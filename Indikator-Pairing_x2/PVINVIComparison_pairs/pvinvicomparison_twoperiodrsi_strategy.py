import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
