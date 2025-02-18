import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
