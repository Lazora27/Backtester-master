import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'VortexIndicator': 1.0
        })
    )
