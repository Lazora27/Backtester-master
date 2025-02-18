import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CenterOfGravity': 1.0
        })
    )
