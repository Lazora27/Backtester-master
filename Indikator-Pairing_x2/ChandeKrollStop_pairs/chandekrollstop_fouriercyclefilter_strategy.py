import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
