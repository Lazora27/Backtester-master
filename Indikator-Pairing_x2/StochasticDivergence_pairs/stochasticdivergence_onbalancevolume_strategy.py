import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
