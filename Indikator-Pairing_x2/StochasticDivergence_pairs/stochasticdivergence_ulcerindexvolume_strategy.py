import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
