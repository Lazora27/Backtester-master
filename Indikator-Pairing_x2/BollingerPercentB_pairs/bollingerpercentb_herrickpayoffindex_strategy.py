import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
