import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AdaptiveATR': 1.0
        })
    )
