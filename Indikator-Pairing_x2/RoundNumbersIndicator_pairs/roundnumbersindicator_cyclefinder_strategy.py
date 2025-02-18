import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
