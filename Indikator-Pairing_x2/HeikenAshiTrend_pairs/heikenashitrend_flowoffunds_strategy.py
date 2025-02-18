import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'FlowOfFunds': 1.0
        })
    )
