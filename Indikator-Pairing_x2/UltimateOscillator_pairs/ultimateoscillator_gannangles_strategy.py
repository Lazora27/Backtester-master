import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und GannAngles
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'GannAngles': 1.0
        })
    )
