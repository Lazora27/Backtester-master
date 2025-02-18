import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'BollingerPercentB': 1.0
        })
    )
