import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
