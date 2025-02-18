import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AndrewsPitchfork_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AndrewsPitchfork und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AndrewsPitchfork': 1.0,
            'ProjectionBands': 1.0
        })
    )
