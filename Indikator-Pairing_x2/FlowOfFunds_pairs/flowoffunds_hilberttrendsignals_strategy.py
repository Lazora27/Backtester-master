import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
