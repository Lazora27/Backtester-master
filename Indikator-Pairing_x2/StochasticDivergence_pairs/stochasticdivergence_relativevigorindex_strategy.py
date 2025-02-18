import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
