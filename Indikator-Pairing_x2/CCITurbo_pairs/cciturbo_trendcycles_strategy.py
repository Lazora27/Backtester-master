import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'TrendCycles': 1.0
        })
    )
