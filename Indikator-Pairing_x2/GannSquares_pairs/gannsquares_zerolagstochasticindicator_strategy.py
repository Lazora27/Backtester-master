import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
