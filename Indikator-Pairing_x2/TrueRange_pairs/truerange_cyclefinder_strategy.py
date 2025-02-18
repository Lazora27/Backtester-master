import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'CycleFinder': 1.0
        })
    )
