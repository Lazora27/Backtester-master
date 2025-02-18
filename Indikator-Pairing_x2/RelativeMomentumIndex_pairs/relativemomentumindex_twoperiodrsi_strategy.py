import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
