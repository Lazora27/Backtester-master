import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
