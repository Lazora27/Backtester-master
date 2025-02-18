import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und CycleFinder
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'CycleFinder': 1.0
        })
    )
