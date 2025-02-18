import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'AverageLogRange': 1.0
        })
    )
