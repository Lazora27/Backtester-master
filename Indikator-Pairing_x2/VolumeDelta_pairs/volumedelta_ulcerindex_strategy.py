import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'UlcerIndex': 1.0
        })
    )
