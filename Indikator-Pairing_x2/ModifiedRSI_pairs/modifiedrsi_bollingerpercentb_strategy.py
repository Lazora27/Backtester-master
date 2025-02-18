import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
