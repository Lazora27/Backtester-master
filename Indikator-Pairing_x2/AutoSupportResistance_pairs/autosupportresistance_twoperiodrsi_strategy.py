import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
