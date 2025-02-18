import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
