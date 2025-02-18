import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
