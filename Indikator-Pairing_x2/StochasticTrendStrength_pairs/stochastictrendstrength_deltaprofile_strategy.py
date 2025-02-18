import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'DeltaProfile': 1.0
        })
    )
