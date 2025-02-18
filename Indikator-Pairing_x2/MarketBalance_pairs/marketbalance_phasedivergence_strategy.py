import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'PhaseDivergence': 1.0
        })
    )
