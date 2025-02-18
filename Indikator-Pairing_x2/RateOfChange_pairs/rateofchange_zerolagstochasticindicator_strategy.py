import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_ZeroLagStochasticIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und ZeroLagStochasticIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'ZeroLagStochasticIndicator': 1.0
        })
    )
