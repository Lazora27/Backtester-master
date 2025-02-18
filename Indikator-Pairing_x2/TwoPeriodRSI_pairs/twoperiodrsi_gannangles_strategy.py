import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'GannAngles': 1.0
        })
    )
