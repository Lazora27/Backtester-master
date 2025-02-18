import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
