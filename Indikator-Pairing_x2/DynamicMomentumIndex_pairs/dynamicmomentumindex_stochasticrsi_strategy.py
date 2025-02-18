import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
