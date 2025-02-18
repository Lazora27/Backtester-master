import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagStochasticIndicator_TTMSqueezeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagStochasticIndicator und TTMSqueezeIndicator
    """
    
    params = (
        ('indicators', {
            'ZeroLagStochasticIndicator': {
                'class': ZeroLagStochasticIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagStochasticIndicator'>
            },
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            }
        }),
        ('weights', {
            'ZeroLagStochasticIndicator': 1.0,
            'TTMSqueezeIndicator': 1.0
        })
    )
