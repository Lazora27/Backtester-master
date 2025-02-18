import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
