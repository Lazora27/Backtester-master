import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
