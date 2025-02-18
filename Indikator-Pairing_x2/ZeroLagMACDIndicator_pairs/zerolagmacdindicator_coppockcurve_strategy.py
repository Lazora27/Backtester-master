import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ZeroLagMACDIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ZeroLagMACDIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ZeroLagMACDIndicator': {
                'class': ZeroLagMACDIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZeroLagMACDIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ZeroLagMACDIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
