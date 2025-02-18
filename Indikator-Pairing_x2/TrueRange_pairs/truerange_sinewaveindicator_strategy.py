import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
