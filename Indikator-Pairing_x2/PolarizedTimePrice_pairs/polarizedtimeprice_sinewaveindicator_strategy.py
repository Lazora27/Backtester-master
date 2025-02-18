import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
