import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
