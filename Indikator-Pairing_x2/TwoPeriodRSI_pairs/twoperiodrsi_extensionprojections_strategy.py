import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
