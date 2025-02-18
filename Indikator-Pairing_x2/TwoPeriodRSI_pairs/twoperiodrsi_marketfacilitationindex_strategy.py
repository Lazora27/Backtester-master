import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
