import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PriceSquawk': 1.0
        })
    )
