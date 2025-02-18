import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
