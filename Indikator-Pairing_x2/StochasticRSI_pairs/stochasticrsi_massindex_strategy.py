import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und MassIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'MassIndex': 1.0
        })
    )
