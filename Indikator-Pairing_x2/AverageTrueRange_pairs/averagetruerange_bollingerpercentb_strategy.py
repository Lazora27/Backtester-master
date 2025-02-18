import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
