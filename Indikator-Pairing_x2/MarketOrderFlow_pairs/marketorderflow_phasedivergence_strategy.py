import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'PhaseDivergence': 1.0
        })
    )
