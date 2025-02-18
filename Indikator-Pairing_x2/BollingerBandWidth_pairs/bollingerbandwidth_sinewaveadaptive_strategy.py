import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
