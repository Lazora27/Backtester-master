import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'BarStrength': 1.0
        })
    )
