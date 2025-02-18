import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PriceDelta
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PriceDelta': 1.0
        })
    )
