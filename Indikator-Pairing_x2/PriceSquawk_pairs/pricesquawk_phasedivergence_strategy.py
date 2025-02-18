import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'PhaseDivergence': 1.0
        })
    )
