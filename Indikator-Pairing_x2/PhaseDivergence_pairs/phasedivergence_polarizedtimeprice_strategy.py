import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
