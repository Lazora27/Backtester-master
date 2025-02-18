import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'AroonIndicator': 1.0
        })
    )
