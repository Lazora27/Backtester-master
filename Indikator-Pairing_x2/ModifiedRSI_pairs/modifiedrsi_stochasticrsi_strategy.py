import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'StochasticRSI': 1.0
        })
    )
