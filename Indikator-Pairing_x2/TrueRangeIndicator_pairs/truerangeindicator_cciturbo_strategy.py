import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'CCITurbo': 1.0
        })
    )
