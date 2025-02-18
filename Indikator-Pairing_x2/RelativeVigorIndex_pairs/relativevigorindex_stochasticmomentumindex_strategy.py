import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
