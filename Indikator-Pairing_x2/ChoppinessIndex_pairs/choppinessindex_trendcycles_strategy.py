import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
