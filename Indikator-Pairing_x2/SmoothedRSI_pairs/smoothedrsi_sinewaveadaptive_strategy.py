import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
