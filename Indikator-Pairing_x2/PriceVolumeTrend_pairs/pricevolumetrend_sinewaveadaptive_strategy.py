import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
