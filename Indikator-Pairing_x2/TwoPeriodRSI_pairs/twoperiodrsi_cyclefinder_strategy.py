import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CycleFinder
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CycleFinder': 1.0
        })
    )
