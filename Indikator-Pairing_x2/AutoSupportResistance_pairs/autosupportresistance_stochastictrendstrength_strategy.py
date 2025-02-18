import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
