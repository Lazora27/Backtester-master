import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
