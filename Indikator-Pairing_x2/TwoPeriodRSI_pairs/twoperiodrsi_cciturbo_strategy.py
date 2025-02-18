import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CCITurbo
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CCITurbo': 1.0
        })
    )
