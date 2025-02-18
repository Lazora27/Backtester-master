import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
