import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TimeCycle
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TimeCycle': 1.0
        })
    )
