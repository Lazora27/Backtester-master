import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
