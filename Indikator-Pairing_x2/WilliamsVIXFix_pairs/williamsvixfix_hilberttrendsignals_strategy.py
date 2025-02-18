import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
