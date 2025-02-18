import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
