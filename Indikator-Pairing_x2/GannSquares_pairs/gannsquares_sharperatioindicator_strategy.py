import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
