import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'PhaseDivergence': 1.0
        })
    )
