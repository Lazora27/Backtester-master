import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
