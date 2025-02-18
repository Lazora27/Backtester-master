import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
