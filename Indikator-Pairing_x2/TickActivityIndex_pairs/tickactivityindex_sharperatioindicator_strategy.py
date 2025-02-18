import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
