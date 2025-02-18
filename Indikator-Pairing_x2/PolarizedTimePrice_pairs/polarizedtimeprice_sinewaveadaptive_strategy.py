import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
