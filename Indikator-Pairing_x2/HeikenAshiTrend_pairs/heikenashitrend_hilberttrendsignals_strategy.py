import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
