import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und WilliamsR
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'WilliamsR': 1.0
        })
    )
