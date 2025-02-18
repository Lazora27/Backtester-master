import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und GannFans
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'GannFans': 1.0
        })
    )
