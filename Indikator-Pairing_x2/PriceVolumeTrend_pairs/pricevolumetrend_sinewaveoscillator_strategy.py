import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
