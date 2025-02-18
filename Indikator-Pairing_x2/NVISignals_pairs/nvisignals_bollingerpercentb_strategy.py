import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'BollingerPercentB': 1.0
        })
    )
