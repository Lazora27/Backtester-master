import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
