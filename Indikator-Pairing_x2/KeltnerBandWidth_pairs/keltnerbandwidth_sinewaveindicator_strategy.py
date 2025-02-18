import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
