import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PhaseDivergence': 1.0
        })
    )
