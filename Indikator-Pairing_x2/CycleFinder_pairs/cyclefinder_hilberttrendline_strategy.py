import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CycleFinder_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CycleFinder und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'CycleFinder': 1.0,
            'HilbertTrendline': 1.0
        })
    )
