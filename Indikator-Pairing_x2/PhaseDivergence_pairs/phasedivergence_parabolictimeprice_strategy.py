import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PhaseDivergence_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PhaseDivergence und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PhaseDivergence': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
