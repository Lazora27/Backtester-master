import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ModifiedATR': 1.0
        })
    )
