import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
