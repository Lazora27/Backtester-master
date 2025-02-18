import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BuyingPressure': 1.0
        })
    )
