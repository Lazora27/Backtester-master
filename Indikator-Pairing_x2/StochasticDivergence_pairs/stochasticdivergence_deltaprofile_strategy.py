import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DeltaProfile': 1.0
        })
    )
