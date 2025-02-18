import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
