import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'StochasticRSI': 1.0
        })
    )
