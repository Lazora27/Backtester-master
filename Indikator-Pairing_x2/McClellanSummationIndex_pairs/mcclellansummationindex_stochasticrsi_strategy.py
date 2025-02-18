import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
