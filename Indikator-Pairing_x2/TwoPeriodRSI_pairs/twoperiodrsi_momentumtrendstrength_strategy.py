import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
