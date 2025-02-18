import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'BollingerPercentB': 1.0
        })
    )
