import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
