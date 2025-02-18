import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_ArmsEaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und ArmsEaseOfMovement
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'ArmsEaseOfMovement': {
                'class': ArmsEaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsEaseOfMovement'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'ArmsEaseOfMovement': 1.0
        })
    )
