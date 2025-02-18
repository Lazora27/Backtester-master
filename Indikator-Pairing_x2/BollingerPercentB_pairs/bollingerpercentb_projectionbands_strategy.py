import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'ProjectionBands': 1.0
        })
    )
