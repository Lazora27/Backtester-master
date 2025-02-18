import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und CCITurbo
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'CCITurbo': 1.0
        })
    )
