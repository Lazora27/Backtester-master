import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FlowOfFunds': 1.0
        })
    )
