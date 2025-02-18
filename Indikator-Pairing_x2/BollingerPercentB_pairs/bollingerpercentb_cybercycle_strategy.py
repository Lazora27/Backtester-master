import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und CyberCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'CyberCycle': 1.0
        })
    )
