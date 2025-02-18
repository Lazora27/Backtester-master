import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PhaseDivergence': 1.0
        })
    )
