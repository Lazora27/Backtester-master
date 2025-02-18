import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
