import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'PhaseDivergence': 1.0
        })
    )
