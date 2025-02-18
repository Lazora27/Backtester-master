import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
