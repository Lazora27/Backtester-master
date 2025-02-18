import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
