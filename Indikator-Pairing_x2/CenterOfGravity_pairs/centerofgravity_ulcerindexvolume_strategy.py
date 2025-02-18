import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
