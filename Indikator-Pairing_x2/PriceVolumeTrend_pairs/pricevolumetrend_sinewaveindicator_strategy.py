import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
