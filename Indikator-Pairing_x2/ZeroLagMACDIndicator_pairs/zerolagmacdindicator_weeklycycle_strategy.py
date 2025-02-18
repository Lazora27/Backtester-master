import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'WeeklyCycle': 1.0
        })
    )
