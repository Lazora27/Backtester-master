import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
