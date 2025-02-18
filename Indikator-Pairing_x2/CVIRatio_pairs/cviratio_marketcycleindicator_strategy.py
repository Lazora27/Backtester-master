import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
