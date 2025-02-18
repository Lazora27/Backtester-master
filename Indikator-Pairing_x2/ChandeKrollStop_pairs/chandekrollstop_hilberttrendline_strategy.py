import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'HilbertTrendline': 1.0
        })
    )
