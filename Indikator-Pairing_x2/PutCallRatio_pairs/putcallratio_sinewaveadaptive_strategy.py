import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
