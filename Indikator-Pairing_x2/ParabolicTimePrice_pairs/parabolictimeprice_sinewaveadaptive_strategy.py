import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ParabolicTimePrice_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ParabolicTimePrice und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ParabolicTimePrice': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
