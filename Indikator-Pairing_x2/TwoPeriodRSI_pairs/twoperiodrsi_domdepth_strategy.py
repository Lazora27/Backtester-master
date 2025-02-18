import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DOMDepth
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DOMDepth': 1.0
        })
    )
