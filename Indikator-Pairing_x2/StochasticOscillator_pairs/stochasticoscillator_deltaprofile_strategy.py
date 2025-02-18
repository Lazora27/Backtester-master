import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
