import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
