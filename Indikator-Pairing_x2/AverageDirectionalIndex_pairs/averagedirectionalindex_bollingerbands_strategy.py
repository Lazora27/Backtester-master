import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
