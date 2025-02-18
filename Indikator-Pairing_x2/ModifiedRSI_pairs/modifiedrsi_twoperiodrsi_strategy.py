import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
