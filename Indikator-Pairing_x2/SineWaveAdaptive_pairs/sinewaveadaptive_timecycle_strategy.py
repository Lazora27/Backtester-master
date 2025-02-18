import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'TimeCycle': 1.0
        })
    )
