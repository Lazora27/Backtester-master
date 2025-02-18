import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
