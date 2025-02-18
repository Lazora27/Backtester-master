import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
