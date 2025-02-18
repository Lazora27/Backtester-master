import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
