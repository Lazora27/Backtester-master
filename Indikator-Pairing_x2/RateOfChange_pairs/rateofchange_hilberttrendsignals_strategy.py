import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
