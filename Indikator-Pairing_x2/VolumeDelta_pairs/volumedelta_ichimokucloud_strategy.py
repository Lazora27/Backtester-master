import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'IchimokuCloud': 1.0
        })
    )
