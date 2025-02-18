import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
