import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
