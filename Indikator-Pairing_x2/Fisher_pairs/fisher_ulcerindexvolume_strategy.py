import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
