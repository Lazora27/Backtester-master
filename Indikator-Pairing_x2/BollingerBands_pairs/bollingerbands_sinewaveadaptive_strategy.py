import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
