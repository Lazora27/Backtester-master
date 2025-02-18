import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
