import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
