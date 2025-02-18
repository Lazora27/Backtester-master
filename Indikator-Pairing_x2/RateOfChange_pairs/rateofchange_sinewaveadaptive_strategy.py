import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
