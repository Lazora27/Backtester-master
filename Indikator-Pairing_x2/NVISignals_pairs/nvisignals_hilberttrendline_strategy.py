import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'HilbertTrendline': 1.0
        })
    )
