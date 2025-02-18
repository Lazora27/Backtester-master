import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
