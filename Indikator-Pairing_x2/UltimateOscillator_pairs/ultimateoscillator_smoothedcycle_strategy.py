import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SmoothedCycle': 1.0
        })
    )
