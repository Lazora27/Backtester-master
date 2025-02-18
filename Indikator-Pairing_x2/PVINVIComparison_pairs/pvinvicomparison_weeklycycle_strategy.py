import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'WeeklyCycle': 1.0
        })
    )
