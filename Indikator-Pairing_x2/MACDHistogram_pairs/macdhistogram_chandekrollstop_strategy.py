import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
