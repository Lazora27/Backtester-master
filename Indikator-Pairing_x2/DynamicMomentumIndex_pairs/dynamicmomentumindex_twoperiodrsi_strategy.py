import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_TwoPeriodRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und TwoPeriodRSI
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'TwoPeriodRSI': 1.0
        })
    )
