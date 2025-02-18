import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'WolfeWaves': 1.0
        })
    )
