import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
