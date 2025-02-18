import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und CycleFinder
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'CycleFinder': 1.0
        })
    )
