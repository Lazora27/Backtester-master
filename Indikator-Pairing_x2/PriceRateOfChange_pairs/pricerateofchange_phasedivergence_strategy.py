import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'PhaseDivergence': 1.0
        })
    )
