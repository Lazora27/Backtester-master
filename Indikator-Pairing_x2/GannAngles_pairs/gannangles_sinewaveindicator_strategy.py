import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
