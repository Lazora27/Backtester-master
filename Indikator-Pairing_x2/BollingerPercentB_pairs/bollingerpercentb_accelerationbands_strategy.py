import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'AccelerationBands': 1.0
        })
    )
