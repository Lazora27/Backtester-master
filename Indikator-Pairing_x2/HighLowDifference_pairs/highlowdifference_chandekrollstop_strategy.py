import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ChandeKrollStop_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ChandeKrollStop
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ChandeKrollStop': 1.0
        })
    )
