import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'CycleFinder': 1.0
        })
    )
