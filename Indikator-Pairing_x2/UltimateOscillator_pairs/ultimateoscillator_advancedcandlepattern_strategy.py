import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
