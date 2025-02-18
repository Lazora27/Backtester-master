import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'GannFans': 1.0
        })
    )
