import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
