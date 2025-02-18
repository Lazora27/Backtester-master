import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
