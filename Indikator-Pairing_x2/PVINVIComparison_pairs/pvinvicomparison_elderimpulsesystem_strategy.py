import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
