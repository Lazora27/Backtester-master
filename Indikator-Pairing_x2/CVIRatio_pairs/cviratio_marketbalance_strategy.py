import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketBalance
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketBalance': 1.0
        })
    )
