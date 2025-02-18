import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolumeDelta': 1.0
        })
    )
