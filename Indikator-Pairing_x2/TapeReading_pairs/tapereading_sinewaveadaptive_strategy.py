import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
