import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StandardDeviationIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StandardDeviationIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StandardDeviationIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
