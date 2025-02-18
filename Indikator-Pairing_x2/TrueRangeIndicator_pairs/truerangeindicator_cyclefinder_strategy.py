import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
