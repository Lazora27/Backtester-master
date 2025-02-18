import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
