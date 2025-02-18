import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
