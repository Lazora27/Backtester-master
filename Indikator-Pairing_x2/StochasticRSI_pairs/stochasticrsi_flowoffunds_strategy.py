import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'FlowOfFunds': 1.0
        })
    )
