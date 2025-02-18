import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UlcerIndexVolume_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UlcerIndexVolume und CCITurbo
    """
    
    params = (
        ('indicators', {
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'UlcerIndexVolume': 1.0,
            'CCITurbo': 1.0
        })
    )
