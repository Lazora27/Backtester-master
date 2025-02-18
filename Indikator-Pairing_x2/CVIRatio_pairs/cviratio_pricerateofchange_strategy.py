import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
