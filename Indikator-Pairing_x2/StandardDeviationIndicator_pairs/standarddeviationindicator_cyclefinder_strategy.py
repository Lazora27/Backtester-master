import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
