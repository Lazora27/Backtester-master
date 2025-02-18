import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
