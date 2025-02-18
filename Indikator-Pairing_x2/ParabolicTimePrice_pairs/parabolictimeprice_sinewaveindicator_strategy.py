import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
