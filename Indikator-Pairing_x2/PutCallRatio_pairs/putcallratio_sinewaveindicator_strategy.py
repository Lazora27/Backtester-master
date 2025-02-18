import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
