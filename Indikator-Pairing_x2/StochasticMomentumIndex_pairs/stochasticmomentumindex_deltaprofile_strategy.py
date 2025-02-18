import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'DeltaProfile': 1.0
        })
    )
