import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
