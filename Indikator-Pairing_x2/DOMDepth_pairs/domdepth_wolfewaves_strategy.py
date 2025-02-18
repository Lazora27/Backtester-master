import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'WolfeWaves': 1.0
        })
    )
