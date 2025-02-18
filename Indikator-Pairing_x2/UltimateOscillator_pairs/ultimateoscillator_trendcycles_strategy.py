import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
