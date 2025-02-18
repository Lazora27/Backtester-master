import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_ZeroLagMACDIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und ZeroLagMACDIndicator
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'ZeroLagMACDIndicator': 1.0
        })
    )
