import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
