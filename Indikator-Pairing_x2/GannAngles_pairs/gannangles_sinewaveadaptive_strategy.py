import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
